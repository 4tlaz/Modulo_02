import sqlite3

conexao = sqlite3.connect("tarefas.sqlite3")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    data_limite DATE,
    categoria_id INTEGER,
    concluido INTEGER DEFAULT 0,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
"""
)


conexao.commit()
conexao.close()