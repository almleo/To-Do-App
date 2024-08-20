import flet as ft

from flet import(
	Page,
	Text,
	TextField,
	FloatingActionButton,
	Row,
	Column,
	Checkbox,
	IconButton,
	Tabs,
	Tab,
	OutlinedButton
	)
import Main

class TodoApp(Column):
	def __init__(self):
		super().__init__()
		self.new_task = TextField(label="O que precisa ser feito?", expand=True)
		self.add_task_btn = FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_task)
		self.column_tasks = Column()
		self.linha = Row(controls = [self.new_task, self.add_task_btn])
		self.width = 600

		self.tarefas = Main.listar_todas_tarefas()

		self.filter = Tabs(
			selected_index = 0,
			on_change=self.tabs_changed,
			tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")]
			)

		self.footer = Footer(self.delete_copleted_task)
		self.controls = [self.linha, self.filter, self.column_tasks, self.footer]

	def add_task(self,event):
		if self.new_task.value != "":
			id = Main.cria_tarefa(self.new_task.value,self.new_task.value,'') # persiste no banco
			task = self.list_espc_task(id)
			self.column_tasks.controls.append(task) # adiciona a GUI lista de tarefas
			
			self.new_task.value = ''
			self.update()

	def list_all_tasks(self):
		for i in self.tarefas:
			task = GuiTask(task_name=i[1], task_status_change=self.task_status_change, task_delete=self.remove_task)
			task.task_id.value=i[0]
			task.display_task.value = True if i[2]==1 else False
			self.column_tasks.controls.append(task)
	
	def list_espc_task(self, id):
		task_db = Main.busca_tarefa(id) # busca a ultima tarefa adicionada

		task_gui = GuiTask(task_db[0][1], task_status_change=self.task_status_change,task_delete=self.remove_task) # cria uma nova GuiTask
		task_gui.task_id.value = task_db[0][0] # configura seu id
		return task_gui
	
	def remove_task(self,task):
		self.column_tasks.controls.remove(task)
		self.update()

	def tabs_changed(self, event):
		self.update()
	
	def task_status_change(self, event):
		self.update()

	def before_update(self):
		count = 0
		status = self.filter.tabs[self.filter.selected_index].text
		for task in self.column_tasks.controls:
			task.visible = (
				status == "all"
				or (status == "active" and task.display_task.value == False)
				or (status == "completed" and task.display_task.value == True)
			)
			if task.display_task.value == False:
				count +=1
		self.footer.items_left.value = f"{count} Tarefa(s) Pendentes"
	
	def delete_copleted_task(self,event):
		for task in self.column_tasks.controls[:]:
			
			if task.display_task.value == True:
				id = task.task_id.value
				task.delete_task(id)
		

		

class GuiTask(Column):
	def __init__(self, task_name, task_status_change, task_delete):
		super().__init__()
		self.task_name = task_name
		self.task_id = Text("0", visible=False)
		self.task_delete = task_delete
		self.task_status_change = task_status_change
		self.btn_edit = IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.edit_task)
		self.btn_delete = IconButton(icon=ft.icons.DELETE_OUTLINED, tooltip="Delete", on_click=self.delete_task)
		self.display_task = Checkbox(value = False, label=self.task_name, on_change=self.update_status)
		self.edit_task_name = TextField(expand=True)

		self.display_view = Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.task_id, self.display_task, Row(controls=[self.btn_edit, self.btn_delete])]
			)

		self.btn_save = IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, tooltip="Save changes", on_click=self.save_change)
		self.edit_view = Row(
			visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
			controls=[self.edit_task_name, self.btn_save]
			)

		self.controls = [self.display_view, self.edit_view]

	
	def edit_task(self, event):
		self.edit_task_name.value = self.display_task.label
		self.display_view.visible=False
		self.edit_view.visible=True

		self.update()

	def save_change(self,event):
		if self.display_task.label != self.edit_task_name.value:
			self.display_task.label = self.edit_task_name.value
			Main.atualiza_tarefa(self.edit_task_name.value, self.display_task.value, self.task_id.value)
		self.display_view.visible=True
		self.edit_view.visible=False

		self.update()

	def update_status(self,event):
		Main.atualiza_tarefa(self.display_task.label, self.display_task.value, self.task_id.value)
		self.task_status_change(event)
		self.update()

	def delete_task(self,event):
		Main.deleta_tarefa(self.task_id.value)
		self.task_delete(self)


class Footer(Column):
	def __init__(self,delete_copleted_task):
		super().__init__()
		self.items_left = Text()
		self.clear_btn = OutlinedButton(text="Clear Completed", on_click=self.delete_completed_task)
		self.delete_copleted_task = delete_copleted_task
		self.width = 600
		self.row_footer = Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[self.items_left, self.clear_btn])
		self.controls=[self.row_footer]
	
	def delete_completed_task(self, event):
		self.delete_copleted_task(event)

		


def main(page: Page):
	page.title = 'Testes Aleatorios'
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.scroll=ft.ScrollMode.ALWAYS
	todo = TodoApp()
	todo.list_all_tasks()
	page.update()

	

	page.add(todo)

ft.app(target=main)