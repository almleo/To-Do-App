# Agendador de Tarefas
# - Classe: Tarefas
# - Atributos: titulo, descricao, data vencimento
# - Métodos: adicionar(), editar(), excluir(), feito(), buscar()



class Tarefa:
  def __init__(self, titulo, descricao, data_vencimento, status):
    self.titulo = titulo
    self.descricao = descricao
    self.data_vencimento = data_vencimento
    self.status = status

  def __str__(self):
    return f"Titulo: {self.titulo} | Descricao: {self.descricao} | Data Limite: {self.data_vencimento} | Status: {self.status} "


  def get_titulo(self):
    return self.titulo

  def get_descricao(self):
    return self. descricao

  def get_data_vencimento(self):
    return self. data_vencimento

  def get_status(self):
    return self.status


  def set_titulo(self,valor):
    self.titulo = valor

  def set_descricao(self,valor):
    self. descricao = valor

  def set_data_vencimento(self,valor):
    self. data_vencimento = valor

  def set_status(self,valor):
    self.status = valor