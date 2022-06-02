import os
os.remove('escola.db') if os.path.exists('escola.db') else None

import sqlite3
conexao = sqlite3.connect('escola.db') # estabelece a conexao com a database, caso ela nao exista, cria o database nomeado
type(conexao) # verifica o tipo da variavel conexao

cur = conexao.cursor() # cria um cursor com base na variavel conexao (que armazena a conexão com a database)
type(cur) # verifica o tipo da variavel cur

sql_create = 'CREATE TABLE cursos (id INTEGER PRIMARY KEY,  titulo VARCHAR (100), categoria VARCHAR (140))'
cur.execute(sql_create)

sql_insert = 'INSERT INTO cursos VALUES (?, ?, ?)'
dataset = [(1000, 'Ciência de Dados', 'Data Science'), (1001, 'Big Data Fundamentos', 'Big Data'), (1002, 'Python Fundamentos', 'Análise de Dados')]

for item in dataset:
    cur.execute(sql_insert, item)

conexao.commit()