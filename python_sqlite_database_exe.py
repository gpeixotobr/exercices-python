import sqlite3
import random
import time
import datetime

# Criar uma conexão (ou criar o banco de dados caso ele ainda não exista)
con = sqlite3.connect('database.db')

# Criar um cursor
cur = con.cursor()

# Definir uma função para criação de uma tabela
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date VARCHAR(250), name VARCHAR(250), price REAL)')

# Definir uma função de inserção de dados na tabela
def insert_database():
    new_date = datetime.datetime.now()
    new_name = 'Monitor'
    new_price = random.random()*50 + 50
    cur.execute('INSERT INTO produtos(date, name, price) VALUES (?, ?, ?)', (new_date, new_name, new_price))
    con.commit()

for item in range(10):
    insert_database()
    time.sleep(1)


#Fechar o cursor e a conexão
cur.close()
con.close()
