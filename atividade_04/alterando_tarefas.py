import sqlite3

conexao = sqlite3.connect("tarefas.sqlite3")
cursor = conexao.cursor()

# Criar tarefa
def criar_tarefa(descricao, data_limite, categoria_id):
    cursor.execute("INSERT INTO tarefas (descricao, data_limite, categoria_id) VALUES (?, ?, ?)",
                   (descricao, data_limite, categoria_id))
    conexao.commit()

# Atualizar tarefa
def atualizar_tarefa(tarefa_id, descricao, data_limite, categoria_id, concluido):
    cursor.execute("UPDATE tarefas SET descricao=?, data_limite=?, categoria_id=?, concluido=? WHERE id=?",
                   (descricao, data_limite, categoria_id, concluido, tarefa_id))
    conexao.commit()

# Excluir tarefa
def excluir_tarefa(tarefa_id):
    cursor.execute("DELETE FROM tarefas WHERE id=?", (tarefa_id,))
    conexao.commit()

# Marcar tarefa como concluída
def marcar_como_concluido(tarefa_id):
    cursor.execute("UPDATE tarefas SET concluido=1 WHERE id=?", (tarefa_id,))
    conexao.commit()


conexao.commit()
conexao.close()