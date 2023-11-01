from produto import add_produto, delete_produto, read_produto, update_produto
from usuario import add_compra, create_usuario, delete_compra, delete_favorito, read_usuario, update_usuario, delete_usuario, add_favorito
from vendedor import add_vendedor, adicionar_avaliacao, atualizar_produto, cadastro_produto, listar_produtos,read_vendedor, remover_produto,update_vendedor,delete_vendedor

key = 0
sub = 0
while (key != 'S' and key != 's'):
    print("|---------------------Bem Vindo---------------------------------|")
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("|---------------------------------------------------------------|")
    key = input("Digite a opção desejada? (S para sair) ")
    print ("")

    if (key == '1'):
        print("|-------------------Menu do Usuário---------------------------|")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        print("|--------------------Funcionalidades--------------------------|")
        print("5-Adicionar Favoritos")
        print("6-Remover Favoritos")
        print("7-Adicionar Compra")
        print("8-Cancelar Compra")
        print("|--------------------------------------------------------------|")
        sub = input("Digite a opção desejada? (V para voltar) ")
        print ("")

        if (sub == '1'):
            print("|-------------------Criação de Usuário------------------------|")
            create_usuario()
            print ("")
            
        elif (sub == '2'):
            print("|----------------Listagem de Usuário-------------------------|")
            read_usuario()
            print ("")
        
        elif (sub == '3'):
            print("|--------------------------------------------------------------|")
            update_usuario()
            print ("")

        elif (sub == '4'):
            print("|--------------------------------------------------------------|")
            delete_usuario()
            print ("")
        
        elif (sub == '5'):
            print("|--------------------------------------------------------------|")
            cpf = input("Digite o cpf do usuário que deseja adicionar favoritos: ")
            add_favorito(cpf)
            print ("")
        
        elif (sub == '6'):
            print("|--------------------------------------------------------------|")
            cpf = input("Digite o cpf do usuário que deseja remover favoritos: ")
            delete_favorito(cpf)
            print ("")

        elif (sub == '7'):
            print("|--------------------------------------------------------------|")
            cpf = input("Digite o cpf do usuário que deseja adicionar compra: ")
            add_compra(cpf)
            print ("")
        
        elif (sub == '8'):
            print("|--------------------------------------------------------------|")
            cpf = input("Digite o cpf do usuário que deseja cancelar compra: ")
            delete_compra(cpf)
            print ("")
            
    elif (key == '2'):
         print("|-------------------Menu do Vendedor---------------------------|")
         print("1-Create Vendedor")
         print("2-Read Vendedor")
         print("3-Update Vendedor")
         print("4-Delete Vendedor")
         print("|--------------------Funcionalidades--------------------------|")
         print("5-Adicionar Produto")
         print("6-Listar Produtos")
         print("7-Atualizar Produto")
         print("8-Remover Produto")
         print("9-Adicionar Avaliação")
         print("|--------------------------------------------------------------|")
         sub = input("Digite a opção desejada? (V para voltar) ")
         print ("") 

         if (sub == '1'):
             print("|-------------------Criação de Vendedor------------------------|")
             add_vendedor()
             print ("")
        
         elif (sub == '2'):
             print("|----------------Listagem de Vendedor-------------------------|")
             read_vendedor()
             print ("")

         elif (sub == '3'):
             print("|--------------------------------------------------------------|")
             nome = input("Digite o nome do vendedor que deseja atualizar: ")
             update_vendedor(nome)
             print ("")   

         elif (sub == '4'):
             print("|--------------------------------------------------------------|")
             nome = input("Digite o nome para deletar o vendedor desejado: ")
             delete_vendedor(nome)
             print ("")
            
         elif (sub == '5'):
             print("|--------------------------------------------------------------|")
             cadastro_produto()
             print ("")
        
         elif (sub == '6'):
            print("|--------------------------------------------------------------|")
            nome = input("Digite o nome do vendedor que deseja listar os produtos: ")
            listar_produtos(nome)
            print ("")
        
         elif (sub == '7'):
             print("|--------------------------------------------------------------|")
             atualizar_produto()
             print ("")
        
         elif (sub == '8'):
             print("|--------------------------------------------------------------|")
             remover_produto()
             print ("")
        
         elif (sub == '9'):
             print("|--------------------------------------------------------------|")
             adicionar_avaliacao()
             print ("")

        
        



    elif (key == '3'):
        print("|----------------------Menu de Produtos------------------------|")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")
        sub = input("Digite a opção desejada? (V para voltar) ")
        print ("")      

        if (sub == '1'):
            print("|-------------------Criação de Produto------------------------|")
            add_produto()
            print ("")

        elif (sub == '2'):
            print("|----------------Listagem de Produto-------------------------|")
            nome = input("Digite o nome do produto ou clique ENTER para listagem dos produtos: ")
            read_produto(nome)
            print ("")
        
        elif (sub == '3'):
            print("|--------------------------------------------------------------|")
            nome = input("Digite o nome do produto que deseja atualizar: ")
            update_produto(nome)
            print ("")
        
        elif (sub == '4'):
            print("|--------------------------------------------------------------|")
            nome = input("Digite o nome para deletar o produto desejado: ")
            delete_produto(nome)
            print ("")
            

print("Vlw Flw...")