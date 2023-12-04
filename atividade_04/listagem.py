import sqlite3

conexao = sqlite3.connect("tarefas.sqlite3")
cursor = conexao.cursor()

def listar_tarefas_do_dia(data):
    cursor.execute("SELECT * FROM tarefas WHERE data_limite=?", (data,))
    tarefas = cursor.fetchall()
    return tarefas

def listar_categorias():
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    return categorias


conexao.commit()
conexao.close()