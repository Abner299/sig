import sqlite3
import replit
replit.clear()

# Conectar ao banco de dados SQLite embutido
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

# Criar tabelas se elas não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_civis (
        nome TEXT,
        cpf TEXT,
        idade INTEGER,
        pai TEXT,
        mae TEXT,
        sexo TEXT,
        nascimento TEXT,
        telefone TEXT
    )
''')
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



cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_criminais (
        num_registro TEXT,
        crime TEXT,
        data TEXT,
        local TEXT,
        cpf_envolvido TEXT,
        incidencia TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros_veiculares (
        Dono TEXT,
        cpf TEXT,
        Modelo TEXT,
        placa TEXT,
        Cor TEXT
    )
''')



def add_mandado():
    numero_mandado = input("Digite o numero de registro: ")
    data_mandado = input("Digite a data de emissão ")
    situacao_mandado = input("Digite a situação aberto/fechado: ")
    tipo_mandado = input("Tipo do mandado,Prisão,busca e apreensão: ")
    acusado_mandado = input("Digite o nome do acusado: ")
    cpf_mandado = input("Digite o cpf do acusado: ")
    crime_mandado = input("Digite os crimes cometidos: ")
    desc_mandado = input("Digite a descrição do mandato")
    emissor_mandado = input("Nome do emissor do mandado")
    
    

    cursor.execute('''
        INSERT INTO registros_bo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (numero_mandado,data_mandado,situacao_mandado,tipo_mandado,acusado_mandado,cpf_mandado,crime_mandado,desc_mandado,emissor_mandado))

    conn.commit()
    print("Mandado cadastrado com Sucesso!.")



 
#adicionar um b.o
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
    num_registro = input("Digite o nome da vítima: ")#18/08/2023, passsa a ser vitima.
    crime = input("Digite o nome do crime: ")
    data = input("Digite a data: ")
    local = input("Digite o local: ")
    cpf_envolvido = input("Digite o CPF do envolvido: ")
    incidencia = input("Digite a incidência: ")

    cursor.execute('''
        INSERT INTO registros_criminais VALUES (?, ?, ?, ?, ?, ?)
    ''', (num_registro, crime, data, local, cpf_envolvido, incidencia))

    conn.commit()
    print("Registro criminal adicionado com sucesso.")

# Adicionar um registro veicular ao banco de dados
def add_vehicular_registry():
    Dono = input("Digite o nome do Dono: ")
    cpf = input("Digite o cpf do dono: ")
    modelo = input("Digite o modelo: ")
    placa = input("Digite a placa: ")
    cor = input("Digite a cor: ")

    cursor.execute('''
        INSERT INTO registros_veiculares VALUES (?, ?, ?, ?, ?)
    ''', (Dono, cpf, modelo, placa, cor))

    conn.commit()
    print("Registro veicular adicionado com sucesso.")








# Pesquisar registro civil por nome
def search_civil_registry():
    valor_pesquisa = input("Digite o nome para pesquisa: ")

    cursor.execute('''
        SELECT * FROM registros_civis WHERE nome LIKE ?
    ''', ('%' + valor_pesquisa + '%',))

    results = cursor.fetchall()
    return results


def search_civil_registry1():
    valor_pesquisa = input("Digite o cpf para pesquisar: ")

    cursor.execute('''
        SELECT * FROM registros_civis WHERE cpf LIKE ?
    ''', ('%' + valor_pesquisa + '%',))

    results = cursor.fetchall()
    return results

# Pesquisar registro criminal por nome
def search_criminal_registry():
    valor_pesquisa = input("Digite o nome para pesquisa: ")

    cursor.execute('''
        SELECT * FROM registros_criminais WHERE cpf_envolvido IN (
            SELECT cpf FROM registros_civis WHERE nome LIKE ?
        )
    ''', ('%' + valor_pesquisa + '%',))

    results = cursor.fetchall()
    return results

# Pesquisar registro veicular por placa
def search_vehicular_registry():
    valor_pesquisa = input("Digite a placa para pesquisa: ")

    cursor.execute('''
        SELECT * FROM registros_veiculares WHERE placa LIKE ?
    ''', ('%' + valor_pesquisa + '%',))

    results = cursor.fetchall()
    return results

# Pesquisar B.O por numero
def search_bo():
    valor_pesquisa = input("Digite o numero para pesquisa: ")

    cursor.execute('''
        SELECT * FROM registros_bo WHERE numero_registro  LIKE ?
    ''', ('%' + valor_pesquisa + '%',))

    results = cursor.fetchall()
    return results







# Função para pesquisar registros criminais vinculados a um CPF
def search_and_print_criminal_registry(cpf):
    cursor.execute('''
        SELECT * FROM registros_criminais WHERE cpf_envolvido = ?
    ''', (cpf,))

    criminal_records = cursor.fetchall()
    if criminal_records:
        print('\033[31m'"\n*** este CPF possui Registros criminais!*** \033[0m")
        
    else:
        print("\n*** Nenhum registro criminal vinculado a este CPF ***")
      





# Função para pesquisar b.o vinculados a um CPF
def search_bo_vinculado(cpf):
    cursor.execute('''
        SELECT * FROM registros_bo WHERE cpf_bo = ?
    ''', (cpf,))

    bo_records = cursor.fetchall()
    if bo_records:
        print('\033[31m'"\n*** este CPF possui B.O em seu nome*** \033[0m")
        for record in bo_records:
            print("Numero do registro:", record[0])
        print("-" * 10)
    else:
        print("\n*** Nenhum b.o vinculado a este CPF ***")
      
#Função para pesquisar mandados vinculados ao cpf
def search_mandado(cpf):
    cursor.execute('''
        SELECT * FROM mandado WHERE cpf_mandado = ?
    ''', (cpf,))

    mandato_records = cursor.fetchall()
    if mandato_records:
        print('\033[31m'"\n*** este CPF possui Mandados em seu nome*** \033[0m")
        for record in mandato_records:
            print("Numero do registro:", record[0], "  ......Situação:",record[2], "......Tipo:",record[3])
    else:
      print("\n*** Nenhum Mandado para este CPF ***")






# Função para pesquisar registros veiculares vinculados a um CPF
def search_and_print_vehicular_registry(cpf):
    cursor.execute('''
        SELECT * FROM registros_veiculares WHERE cpf = ?
    ''', (cpf,))

    vehicular_records = cursor.fetchall()
    if vehicular_records:
        print("\n*** Registros veiculares vinculados a este CPF ***")
        for record in vehicular_records:
            print("Modelo:", record[2],"  Placa:", record[3]) 
          
            
        print("-" * 10)
    else:
        print("\n*** Nenhum registro veicular vinculado a este CPF ***")

# Função para formatar e imprimir os resultados das pesquisas
def format_registry(registry_type, data):
    if registry_type == 'civil':
        print("\nRegistros civis encontrados:")
        for row in data:
            print("Nome:",row[0],"......CPF:",row[1])
            print("Data de Nascimento:",row[6],"......Idade:",row[2])
            print("Mãe:",row[4],"......Pai:", row[3])
            print("Sexo:",row[5],"......Telefone:",row[7])
            

            # Verificar e exibir registros criminais vinculados ao CPF
            search_and_print_criminal_registry(row[1])

            # Verificar e exibir registros veiculares vinculados ao CPF
            search_and_print_vehicular_registry(row[1])
            #Verificar e exibir o B.O
            search_bo_vinculado(row[1])
            search_mandado(row[1])


    elif registry_type == 'bo':
        print("\n B.O Encontrado:")
        for row in data:
            print("Número de Registro:", row[0])
            print("Nome:", row[1])
            print("Cpf:", row[2])
            print("Nome da vitima:", row[3])
            print("Data:", row[4])
            print("Crime:", row[5])
            print("Descrição:", row[6])
            print("-" * 10)
          
    elif registry_type == 'criminal':
        print("\nRegistros criminais encontrados:")
        for row in data:
            print("Nome da vítima:", row[0]) #18/08/2023, passsa a ser vitima.
            print("Crime:", row[1])
            print("Data:", row[2])
            print("Local:", row[3])
            print("CPF do Envolvido:", row[4])
            print("Incidência:", row[5])
            print("-" * 10)
    elif registry_type == 'vehicular':
        print("\nRegistros veiculares encontrados:")
        for row in data:
            print("Dono:", row[0])
            print("CPF:", row[1])
            print("Modelo:", row[2])
            print("Placa:", row[3])
            print("Cor:", row[4])
            print("-" * 10)

# Loop principal do programa
while True:

    print("")
    print('\033[40;1;37m''\033[31m' + "BANCO DE PESQUISA MUNICIPAL\n \033[0m ")
    print('\033[40;1;37m''\033[36m' +"1 - Pesquisa civil por nome \033[0m")
    print('\033[40;1;37m''\033[36m' +"2 - Pesquisa civil por cpf \033[0m")
    print('\033[40;1;37m''\033[31m' +"3 - Pesquisa criminal por nome \033[0m")
    print('\033[40;1;37m''\033[32m' +"4 - Pesquisar veiculos por placa\033[0m")
    print('\033[40;1;37m''\033[36m' +"5 - Pesquisar B.O\033[0m")
    print('\033[40;1;37m''\033[36m' +"6 - Para ir ao menu de cadastro Policial\033[0m")
    




  
    print("0 - Sair")
    option = input("Opção selecionada: ")
    replit.clear()

    if option == "1":
        data = search_civil_registry()
        format_registry('civil', data)
    elif option == "2":
        data = search_civil_registry1()
        format_registry('civil', data)
    elif option == "3":
        data = search_criminal_registry()
        format_registry('criminal', data)
    elif option == "4":
        data = search_vehicular_registry()
        format_registry('vehicular', data)
    elif option == "5":
        data = search_bo()
        format_registry('bo', data)
    elif option == "6":
      exec(open("login_policia.py").read())



    elif option == "9":
      exec(open("main.py").read())
  
    elif option == "0":
        break
    

conn.close()