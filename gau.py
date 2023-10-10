def cadastrar_contato(contatos,nome,numero,email):
    contato={
        'Nome': nome,
        'Numero': numero,
        'Email': email
    }
    contatos.append(contato)
    print("Cliente cadastrado com sucesso!")
    print("----------------------------------")
    print("\n")
contatos=[]

def imprimir_contato (contatos):
    for ID,contato in enumerate(contatos):
        print(f"ID do contato: {ID}")
        print(f"Nome: {contato['Nome']}")
        print(f"Numero : {contato['Numero']}")
        print(f"Email : {contato['Email']}")
        print("-----------------------------")
        print("\n")

def deletar_contato (contatos,ID):
    if 0 <= ID <len(contatos):
        
        del contatos[ID]
        print("contato apagado com sucesso!")

    else:
        print("posição do contato não encontrada")

def atualizar_contato(contatos,numero,nome,email,ID):
    if ID <= len(contatos) and ID < len(contatos):
        contatos[ID]['Nome'] = nome
        contatos[ID]['Numero'] = numero
        contatos[ID]['Email'] = email
    else:
        print("ID INVALIDO")
    print("CONTATO ATUALIZADO")

    
while True:
    print("-----AGENDA DE CONTATOS-------")
    print("1 = CADASTRAR CONTATO")
    print("2 = LISTA DE CONTATOS")
    print("3 = ATUALIZAR CONTATO")
    print("4 = DELETAR CONTATO")
    print("5 = ENCERRAR")
    print("----------------------------------")
    escolha = str(input("escolha uma opção: "))

    if escolha == "1":
        print("--------CADASTRAR CONTATOS----------")
        nome = str(input("Digite o nome do contato: "))
        numero = int(input("Digite o numero do contato: "))
        email = str(input("Digite o email do contato: "))
        cadastrar_contato(contatos,nome,numero,email)

    elif escolha == "2":
        print("-------LISTA DE CONTATOS---------")
        imprimir_contato (contatos)

    elif escolha == "3":
        print("------ATUALIZAR CONTATO--------")
        ID = int(input("Digite o ID do contato: "))
        nome = str(input("Digite o nome: "))
        numero = int(input("Digite o numero: "))
        email = str(input("Digite o email: "))
        atualizar_contato(contatos,numero,nome,email,ID)
        

    elif escolha == "4":
        print("--------DELETAR CONTATOS-----------")
        ID=int(input("digite a posição do contato para apaga-lo: "))
        deletar_contato (contatos,ID)

    elif escolha == "5":
        print("CREdITOS")
        print("Kalvo Runghh")
        print("Dagoberto Botelho Pinto")
        print("Vitor Cabrito")
        break
    else: 
        print("\n")
        print("ESCOLHA INVALIDA!")
        print("\n")