import sqlite3

conexao = sqlite3.connect('fornecedor.db')
cursor = conexao.cursor()

# Inserindo novos dados
cursor.executemany('''
    INSERT INTO fornecedor (id, nome, endereco, produto) 
    VALUES (?, ?, ?, ?);
''', [
    (5, 'Padaria do Pão', 'Rua do Padeiro, 10', 'Pão'),
    (6, 'Marcenaria Martelo', 'Avenida Madeirada, 05', 'Madeira')
])

# Atualizando dados
cursor.execute('''
    UPDATE fornecedor
    SET endereco = 'Rua dos Peixes, 26'
    WHERE id = 2;
''')

# Selecionando todos os dados
cursor.execute('''
    SELECT * FROM fornecedor;
''')

# Selecionando todos os dados com produto igual a Carne
cursor.execute('''
    SELECT * FROM fornecedor
    WHERE produto = 'Carne';
''')

# Removendo dado
cursor.execute('''
    DELETE FROM fornecedor
    WHERE id = 1;
''')

conexao.commit()
conexao.close()


