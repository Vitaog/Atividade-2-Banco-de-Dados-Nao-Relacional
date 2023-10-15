from usuario import add_compra, create_usuario, delete_compra, delete_favorito, read_usuario, update_usuario, delete_usuario, add_favorito

key = 0
sub = 0
while (key != 'S' and key != 's'):
    print("/---------------------Bem Vindo---------------------------------/")
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("/--------------------------------------------------------------/")
    key = input("Digite a opção desejada? (S para sair) ")
    print ("")

    if (key == '1'):
        print("/-------------------Menu do Usuário---------------------------/")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        print("/--------------------Funcionalidades--------------------------/")
        print("5-Adicionar Favoritos")
        print("6-Remover Favoritos")
        print("7-Adicionar Compra")
        print("8-Cancelar Compra")
        print("/--------------------------------------------------------------/")
        sub = input("Digite a opção desejada? (V para voltar) ")
        print ("")

        if (sub == '1'):
            print("/-------------------Criação de Usuário------------------------/")
            create_usuario()
            print ("")
            
        elif (sub == '2'):
            print("/----------------Listagem de Usuário-------------------------/")
            cpf = input("Digite o CPF do usuário ou clique ENTER para listagem dos usuários: ")
            read_usuario(cpf)
            print ("")
        
        elif (sub == '3'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o CPF do usuário que deseja atualizar: ")
            update_usuario(cpf)
            print ("")

        elif (sub == '4'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o cpf para deletar o usuário desejado: ")
            delete_usuario(cpf)
            print ("")
        
        elif (sub == '5'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o cpf do usuário que deseja adicionar favoritos: ")
            add_favorito(cpf)
            print ("")
        
        elif (sub == '6'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o cpf do usuário que deseja remover favoritos: ")
            delete_favorito(cpf)
            print ("")

        elif (sub == '7'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o cpf do usuário que deseja adicionar compra: ")
            add_compra(cpf)
            print ("")
        
        elif (sub == '8'):
            print("/--------------------------------------------------------------/")
            cpf = input("Digite o cpf do usuário que deseja cancelar compra: ")
            delete_compra(cpf)
            print ("")
            
    elif (key == '2'):
        print("Menu do Vendedor")        
    elif (key == '3'):
        print("Menu do Produto")        

print("Vlw Flw...")