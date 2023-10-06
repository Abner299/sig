import subprocess
import sqlite3
import replit
# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

# Criar tabela de usuários se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        senha TEXT
    )
''')


# Função para realizar o login
def realizar_login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    cursor.execute('''
        SELECT * FROM usuarios WHERE usuario = ? AND senha = ?
    ''', (usuario, senha))

    result = cursor.fetchone()

    if result:
        print("Login realizado com sucesso.")
        # Abrir o outro código Python
        subprocess.run(['python', 'Cadastro_policial.py'])
    else:
        print("Usuário ou senha incorretos.")

# Loop principal do programa
while True:
    replit.clear()
    print("Painel de cadastro policial")
    print("1 - Realizar login")
    print("2 - Sair do programa")

    option = input("Opção selecionada: ")

    if option == "1":
        realizar_login()
    elif option == "2":
        break

conn.close()
