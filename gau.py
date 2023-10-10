def imprimir_contato (contato)
    for ID in enumerate(agenda)
        print(f"ID do contato: {ID}")
        print(f"Nome: {agenda['Nome']}")
        print(f"Numero : {agenda['Numero']}")
        print(f"Email : {agenda['Email']}")
        print("==============================")
        print("\n")

def deletar_contato (contato,ID)
    if 0 <= indice <len(contato):
        ID=int(input("digite a posição do contato para apaga-lo: "))
        del agenda[ID]
        print("contato apagado com sucesso!")

    else:
        print("posição do contato não encontrada")
