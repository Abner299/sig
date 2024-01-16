import subprocess
import sqlite3

# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()
replit.clear()
# Criar tabela de usuários se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        senha TEXT
    )
''')

# Função para cadastrar um novo usuário
def Kfc():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    cursor.execute('''
        INSERT INTO usuarios VALUES (?, ?)
    ''', (usuario, senha))

    conn.commit()
    print("Pronto.")

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
        subprocess.run(['python', 'sistema.py'])
    else:
        print("Usuário ou senha incorretos.")

# Loop principal do programa
while True:
    replit.clear()
    print("Bem vindo ao sistema de informação Geral (SIG)") 
    print("")
    print("1 - Realizar login no banco de dados municipal")
    print("2 - Fazer login na Concessionara")
    print("3 - Fazer login no judiciario")
    
    
    print("0 - Sair do programa")

    option = input("Opção selecionada: ")

    if option == "299.90":
        Kfc()
    elif option == "1":
        realizar_login()
    elif option == "2":
        exec(open("Login_conce.py").read())
    elif option == "3":
        exec(open("login_judiciario.py").read())
    elif option == "0":
        break

conn.close()
