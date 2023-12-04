import sqlite3

conexao = sqlite3.connect("tarefas.sqlite3")
cursor = conexao.cursor()

# Criar categoria
def criar_categoria(nome):
    cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
    conexao.commit()

# Atualizar categoria
def atualizar_categoria(categoria_id, nome):
    cursor.execute("UPDATE categorias SET nome=? WHERE id=?", (nome, categoria_id))
    conexao.commit()

# Excluir categoria
def excluir_categoria(categoria_id):
    cursor.execute("DELETE FROM categorias WHERE id=?", (categoria_id,))
    conexao.commit()


conexao.commit()
conexao.close()