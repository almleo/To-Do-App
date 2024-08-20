from Class_Tarefa import Tarefa
import Gerenciador_Conexao as Conexao
import sys
from datetime import datetime

def cria_tarefa(titulo,descricao,data_limite):
	sql = 	'''	INSERT INTO tarefas (titulo, descricao, data_limite, status)	VALUES (%s, %s, %s, %s)	'''
	conn = Conexao.conecta()
	
	data_atual = datetime.today().strftime('%Y-%m-%d')
	

	status = 0
	obj_tarefa = Tarefa(titulo, descricao, data_atual, status)
	
	id = Conexao.executa_insert(conn, sql, obj_tarefa)
	
	return id

def busca_tarefa(id):
	sql = f''' select id, titulo from tarefas where id = {id} '''
	conn = Conexao.conecta()
	tarefa = Conexao.executa_consulta(conn, sql)
	return tarefa
	
def listar_todas_tarefas():
	sql = ''' select id, titulo, status from tarefas '''
	conn = Conexao.conecta()
	
	tarefas = []
	for i in Conexao.executa_consulta(conn, sql):
		tarefas.append(i)
	return tarefas

def atualiza_tarefa(valor, status, id):
	sql = ''' update tarefas set titulo=%s, descricao=%s, status=%s where id = %s '''
	dados = (valor, valor, status, id)
	conn = Conexao.conecta()

	Conexao.executa_update(conn, sql, dados)


def deleta_tarefa(id):
	sql = f'delete from tarefas where id = {id}'

	conn = Conexao.conecta();

	Conexao.executa_delete(conn, sql)
