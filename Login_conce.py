import subprocess
import sqlite3
import replit
# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

# Criar tabela de usuários se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios1 (
        usuario1 TEXT PRIMARY KEY,
        senha1 TEXT
    )
''')

# Função para cadastrar um novo usuário
def Kfc2():
    usuario1 = input("Digite o nome de usuário: ")
    senha1 = input("Digite a senha: ")
    cursor.execute('''
        INSERT INTO usuarios1 VALUES (?, ?)
    ''', (usuario1, senha1))

    conn.commit()
    print("Pronto.")

# Função para realizar o login
def realizar_login():
    usuario1 = input("Digite o nome de usuário: ")
    senha1 = input("Digite a senha: ")

    cursor.execute('''
        SELECT * FROM usuarios1 WHERE usuario1 = ? AND senha1 = ?
    ''', (usuario1, senha1))

    result = cursor.fetchone()

    if result:
        print("Login realizado com sucesso.")
        # Abrir o outro código Python
        subprocess.run(['python', 'cadastro_conce.py'])
    else:
        print("Usuário ou senha incorretos.")

# Loop principal do programa
while True:
    replit.clear()
    print("Fazer login no cadastro de veiculos")
    print("1 - Realizar login")
    print("2 - Sair do programa")

    option = input("Opção selecionada: ")

    if option == "299.90":
        Kfc2()
    elif option == "1":
        realizar_login()
    elif option == "2":
        exec(open("main.py").read())

conn.close()
