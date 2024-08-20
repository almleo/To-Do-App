import mysql.connector
from mysql.connector import Error

def conecta():	
	conexao = None
	try:
		conexao = mysql.connector.connect(
			host='localhost', 
			database='agetaf', 
			user='python', 
			password='', 
			port='3090')
		# print("Connection Successful")

	except Error as err:
		print(f"Erro: {err}")


	return conexao

def executa_insert(conexao, query, val):
	cursor = conexao.cursor()
	last_id = 0
	try:
		cursor.execute(query, ( val.get_titulo(), val.get_descricao(), val.get_data_vencimento(), val.get_status() ))
		last_id = cursor.lastrowid
		conexao.commit()

		return last_id

	except Error as err:
		print(f"Erro: {err} ")

	finally:
		if conexao.is_connected():
			conexao.close()
			# print("Conexao fechada")

def executa_consulta(conexao, query):
	cursor = conexao.cursor()

	try:
		cursor.execute(query)
		return cursor.fetchall()

		
	except Error as err:
		print(f"Erro: {err} ")
	
	finally:
		if conexao.is_connected():
			conexao.close()
			# print("Conexao fechada")

def executa_update(conexao, query, val):
	cursor = conexao.cursor()
	try:
		cursor.execute(query, val)
		conexao.commit()

	except Error as err:
		print(f"Erro: {err} ")

	finally:
		if conexao.is_connected():
			conexao.close()

def executa_delete(conexao, query):
	cursor = conexao.cursor()
	try:
		cursor.execute(query)
		conexao.commit()

		return "Tarefa deletada"

	except Error as err:
		print(f"Erro: {err}")

	finally:
		if conexao.is_connected():
			conexao.close()
			# print("Conexao fechada")

def desconecta(conexao):
	if conexao.is_connected():
		conexao.close()
		# print("Conexao fechada")


# import mysql.connector

# # conexao = mysql.connector.connect(
# # 	host='nome_host', 
# # 	database='nome_banco', 
# # 	user='root', 
# # 	password='', 
# # 	port='3090')

# conexao = mysql.connector.connect(
# 	host='localhost', 
# 	database='testes', 
# 	user='root', 
# 	password='', 
# 	port='3090')

# try:

# 	if conexao.is_connected():
# 		db_info = conexao.get_server_info()
# 		print(f"Informações do servidor: {db_info}")

# 		cursor = conexao.cursor()
# 		cursor.execute("select * from valida")
# 		print(cursor.fetchone())	
	
# except mysql.connector.DatabaseError as err:
# 	print(f"Erro no banco de dados: {err}")
# finally:
# 	if conexao.is_connected():
# 		cursor.close()
# 		conexao.close()
# 		print("Conexao fechada")
	 

# conexao = mysql.connector.connect(
# 	host='nome_host', 
# 	database='nome_banco', 
# 	user='root', 
# 	password='', 
# 	port='3090')

# class Gerenciador_Conexao():
# def __init__(self):


# except mysql.connector.DatabaseError as err:
# print(f"Erro no banco de dados: {err}")
# finally:
# if conexao.is_connected():
# cursor.close()
# conexao.close()
# print("Conexao fechada")

# c1 = conecta()
# c2 = conecta()
# c3 = conecta()
# c4 = conecta()
# c5 = conecta()
# c6 = conecta()
# c7 = conecta()

# print(c1.is_connected())

# executa_consulta(c1,"do sleep(3)")

# print(c1.is_connected())

# desconecta(c1)

# print(c1.is_connected())
