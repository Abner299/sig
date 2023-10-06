import subprocess
import sqlite3
import replit
# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

# Criar tabela de usuários se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios2 (
        usuario2 TEXT PRIMARY KEY,
        senha2 TEXT
    )
''')

def Kfc3():
    usuario2 = input("Digite o nome de usuário: ")
    senha2 = input("Digite a senha: ")

    cursor.execute('''
        INSERT INTO usuarios2 VALUES (?, ?)
    ''', (usuario2, senha2))

    conn.commit()
    print("Pronto.")



# Função para realizar o login
def realizar_login():
    usuario2 = input("Digite o nome de usuário: ")
    senha2 = input("Digite a senha: ")
    cursor.execute('''
        SELECT * FROM usuarios2 WHERE usuario2 = ? AND senha2 = ?
    ''', (usuario2, senha2))

    result = cursor.fetchone()

    if result:
        print("Login realizado com sucesso.")
        # Abrir o outro código Python
        subprocess.run(['python', 'cadastro_judiciario.py'])
    else:
        print("Usuário ou senha incorretos.")

# Loop principal do programa
while True:
    replit.clear()
    print("Painel do judiciario")
    print("1 - Realizar login")
    print("2 - Sair do programa")

    option = input("Opção selecionada: ")

    if option == "1":
        realizar_login()
    elif option == "0":
        break
    elif option == "299.90":
      Kfc3()
conn.close()