import sqlite3
import replit
replit.clear()

# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()








#b.o
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_bo (
        numero_registro TEXT,
        nome TEXT,
        cpf_bo INTEGER,
        nome_vitima TEXT,
        data TEXT,
        crime,
        desc TEXT
        
    )
''')


# Criar tabelas se elas não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_civis (
        nome TEXT,
        cpf TEXT PRIMARY KEY,
        idade INTEGER,
        pai TEXT,
        mae TEXT,
        sexo TEXT,
        nascimento TEXT,
        telefone TEXT
    )
''')




cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_veiculares (
        Dono TEXT,
        cpf TEXT,
        Modelo TEXT,
        placa TEXT PRIMARY KEY,
        Cor TEXT
    )
''')

conn.commit()

# Função para formatar o CPF com hífens
def format_cpf(cpf):
    return "{}-{}-{}".format(cpf[:3], cpf[3:6], cpf[6:])

# Adicionar um registro veicular ao banco de dados
def add_vehicular_registry():
    Dono = input("Digite o nome do Dono: ")
    cpf = input("Insira o cpf do dono: ")
    modelo = input("Digite o modelo: ")
    placa = input("Digite a placa: ")
    cor = input("Digite a cor: ")

    cursor.execute('''
        INSERT INTO registros_veiculares VALUES (?, ?, ?, ?, ?)
    ''', (Dono, cpf,  modelo, placa, cor))

    conn.commit()
    print("Registro veicular adicionado com sucesso.")


def add_bo():
    numero_registro = input("Digite o numero de registro: ")
    nome = input("Digite o nome do suspeito: ")
    cpf_bo = input("Digite o cpf do suspeito: ")
    nome_vitima = input("Digite o nome da vitima: ")
    data = input("Digite a data do fato: ")
    crime = input("Digite o crime: ")
    desc = input("Digite a descrição: ")
    
    

    cursor.execute('''
        INSERT INTO registros_bo VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (numero_registro, nome, cpf_bo, nome_vitima, data, crime, desc))

    conn.commit()
    print("B.O registrado com sucesso.")







# Adicionar um registro civil ao banco de dados
def add_civil_registry():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    cpf = cpf.replace(".", "").replace("-", "")  # Remover quaisquer pontos ou hífens do CPF
    cpf = format_cpf(cpf)  # Formatar o CPF com hífens
    idade = input("Digite a idade: ")
    pai = input("Digite o nome do pai: ")
    mae = input("Digite o nome da mãe: ")
    sexo = input("Digite o sexo: ")
    nascimento = input("Digite a data de nascimento: ")
    telefone = input("Digite o telefone: ")

    cursor.execute('''
        INSERT INTO registros_civis VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, idade, pai, mae, sexo, nascimento, telefone))

    conn.commit()
    print("Registro civil adicionado com sucesso.")

# Adicionar um registro criminal ao banco de dados
def add_criminal_registry():
    cpf = input("Digite o CPF da pessoa: ")

    # Verificar se o CPF existe nos registros civis
    cursor.execute('''
        SELECT nome FROM registros_civis WHERE cpf = ?
    ''', (cpf,))

    result = cursor.fetchone()

    if result:
        nome = result[0]
        num_registro = input("Digite o número de registro: ")
        crime = input("Digite o nome do crime: ")
        data = input("Digite a data: ")
        local = input("Digite o local: ")
        incidencia = input("Digite a incidência: ")

        cursor.execute('''
            INSERT INTO registros_criminais VALUES (?, ?, ?, ?, ?, ?)
        ''', (num_registro, crime, data, local, cpf, incidencia))

        conn.commit()
        print("Registro criminal adicionado com sucesso.")
    else:
        print("CPF não encontrado nos registros civis. Por favor, adicione primeiro o registro civil dessa pessoa.")

# Resto do código (loop principal) conforme fornecido anteriormente...

# Loop principal do programa
while True:
    print("")
    print("BANCO DE DADOS MUNICIPAL")
    print("1 - Adicionar registro veicular ") 
    print("2 - Retornar ao menu SIG ")
    
    

    option = input("Opção selecionada: ")
    replit.clear()

    
    if option == "1":
        add_vehicular_registry()
    elif option == "2":
        exec(open("main.py").read())
    
conn.close()
