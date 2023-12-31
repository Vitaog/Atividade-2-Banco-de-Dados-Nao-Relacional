from produto import add_produto, delete_produto, read_produto, update_produto
from usuario import add_compra, create_usuario, delete_compra, delete_favorito, read_usuario, update_usuario, delete_usuario, add_favorito
from vendedor import add_vendedor, adicionar_avaliacao, atualizar_produto, cadastro_produto, read_vendedor, remover_produto,update_vendedor,delete_vendedor

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
        print("|-------------------Menu do Usuário-----------------------------|")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        print("|--------------------Funcionalidades----------------------------|")
        print("5-Adicionar Favoritos")
        print("6-Remover Favoritos")
        print("7-Adicionar Compra")
        print("8-Cancelar Compra")
        print("|---------------------------------------------------------------|")
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
            add_favorito()
            print ("")
        
        elif (sub == '6'):
            print("|--------------------------------------------------------------|")
            delete_favorito()
            print ("")

        elif (sub == '7'):
            print("|--------------------------------------------------------------|")
            add_compra()
            print ("")
        
        elif (sub == '8'):
            print("|--------------------------------------------------------------|")
            delete_compra()
            print ("")
            
    elif (key == '2'):
         print("|-------------------Menu do Vendedor----------------------------|")
         print("1-Create Vendedor")
         print("2-Read Vendedor")
         print("3-Update Vendedor")
         print("4-Delete Vendedor")
         print("|--------------------Funcionalidades----------------------------|")
         print("5-Adicionar Produto")
         print("6-Atualizar Produto")
         print("7-Remover Produto")
         print("8-Adicionar Avaliação")
         print("|---------------------------------------------------------------|")
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
             update_vendedor()
             print ("")   

         elif (sub == '4'):
             print("|--------------------------------------------------------------|")
             delete_vendedor()
             print ("")
            
         elif (sub == '5'):
             print("|--------------------------------------------------------------|")
             cadastro_produto()
             print ("")
        
         elif (sub == '6'):
             print("|--------------------------------------------------------------|")
             atualizar_produto()
             print ("")
        
         elif (sub == '7'):
             print("|--------------------------------------------------------------|")
             remover_produto()
             print ("")
        
         elif (sub == '8'):
             print("|--------------------------------------------------------------|")
             adicionar_avaliacao()
             print ("")

        
        



    elif (key == '3'):
        print("|----------------------Menu de Produtos-------------------------|")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")
        print("|---------------------------------------------------------------|")
        sub = input("Digite a opção desejada? (V para voltar) ")
        print ("")      

        if (sub == '1'):
            print("|-------------------Criação de Produto-------------------------|")
            add_produto()
            print ("")

        elif (sub == '2'):
            print("|----------------Listagem de Produto-------------------------|")
            read_produto()
            print ("")
        
        elif (sub == '3'):
            print("|--------------------------------------------------------------|")
            update_produto()
            print ("")
        
        elif (sub == '4'):
            print("|--------------------------------------------------------------|")
            delete_produto()
            print ("")
            

print("Vlw Flw...")