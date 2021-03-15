''' MENU 

    [1] - Cadastrar novo contato
    [2] - Ver Contatos
    [3] - Deletar Contato
    [4] - Editar Contato
    [5] - Sair      
    45646565'''
def menu_interacao():
    print("_____MENU_____\n")
    print(' [1] - Cadastrar novo contato\n [2] - Ver contatos\n [3] - Deletar contato\n [4] - Editar contato\n [5] - Sair')
    opcao = int(input("Digite o valor de uma das opções: "))
    return opcao

opcao = menu_interacao()
contatos = []

while opcao != 5:
    if opcao == 1:
        informacoes = []
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone do contato: ")
        email = input("Digite o email do contato: ")
        informacoes.append(nome)
        informacoes.append(telefone)
        informacoes.append(email)
        informacoes.append(" ")
        contatos.append(informacoes)
        opcao = menu_interacao()
    elif opcao == 2:
        for contato in contatos:
            for informacao in contato:
                print(informacao)
        opcao = menu_interacao()
    elif opcao == 3:
        contato_del = input('Digite o nome do contato a ser deletado: ')
        x = 0
        while x < len(contatos):
            if contato_del == contatos[x][0]:
                del contatos[x]
                x += 1
        opcao = menu_interacao()
    elif opcao == 4:
        contato_edi = input("Digite o nome do contato a ser editado: ")
        for contato in contatos:
            if contato_edi == contato[0]:
                nome = input("Digite um novo nome para o contato: ")
                telefone = input("Digite um novo númeor de telefone para o contato: ")
                email = input("Digite um novo email para o contato: ")
                if nome != '':
                    contato[0] = nome
                if telefone != '':
                    contato[1] = telefone
                if email != '':
                    contato[2] = email
        opcao = menu_interacao()