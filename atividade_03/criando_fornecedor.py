import sqlite3

conexao = sqlite3.connect('fornecedor.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedor (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        produto TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO fornecedor (nome, endereco, produto) 
    VALUES (?, ?, ?);
''', [
    ('Empresa de Leite Permaleite', 'Rua dos Leites, 23', 'Leite'),
    ('Peixaria Abril', 'Rua dos Leites, 26', 'Peixe'),
    ('Açougue Legal', 'Rua das Carnes, 30', 'Carne'),
    ('Açougue Novo', 'Rua das Carnes, 50', 'Carne')
])

conexao.commit()
conexao.close()