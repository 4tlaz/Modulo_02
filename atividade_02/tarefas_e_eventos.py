import sqlite3

conexao = sqlite3.connect('gerenciamento.db')
cursor = conexao.cursor()

# Criar tabela de tarefas #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
              id INTEGER PRIMARY KEY,
              nome TEXT NOT NULL,
              data TEXT NOT NULL,
              categoria TEXT,
              status TEXT
    )''')

# Criar tabela de eventos #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
              id INTEGER PRIMARY KEY,
              titulo TEXT NOT NULL,
              data TEXT NOT NULL,
              local TEXT NOT NULL,
              organizador_id INTEGER,
              FOREIGN KEY (organizador_id) REFERENCES organizadores(id)
    )
''')

# Criar tabela de oraganizadores #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS organizadores (
              id INTEGER PRIMARY KEY,
              nome TEXT NOT NULL,
              email TEXT NOT NULL,
              cpf TEXT NOT NULL
    )
''')

conexao.commit()
conexao.close()