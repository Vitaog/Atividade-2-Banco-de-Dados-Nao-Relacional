from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 
import uri

uriMongo = uri.get_db_connection()
# Cria um novo cliente e conecta ao servidor
client = MongoClient(uriMongo, server_api=ServerApi('1'))
global db
db = client.Mercado_Livre

def add_produto():
    global db
    mycol = db.Produto
    print("\nInserindo um novo produto")
    nome_produto = input("Nome do Produto: ")
    descricao = input("Descrição: ")
    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    produto = {
        "nome_produto": nome_produto,
        "descricao": descricao,
        "data_cadastro": data_cadastro
    }

    x = mycol.insert_one(produto)
    print("Produto inserido com ID ", x.inserted_id)

def read_produto():
    global db
    mycol = db.Produto
    print("Produtos existentes: ")
    
    products = list(mycol.find())
    
    if not products:
        print("Nenhum produto encontrado.")
    else:
        for i, produto in enumerate(products, start=1):
            print(f"{i}. {produto['nome_produto']}")
    
    selected_id = input("Selecione um produto pelo ID (ou pressione ENTER para sair): ")
    
    if selected_id:
        try:
            selected_id = int(selected_id)
            if 1 <= selected_id <= len(products):
                selected_product = products[selected_id - 1]
                print(f"Produto: {selected_product['nome_produto']}, Descrição: {selected_product['descricao']}")
            else:
                print("ID inválido.")
        except ValueError:
            print("ID deve ser um número válido.")
    else:
        print("Saindo da leitura de produtos.")

def update_produto():
    global db
    mycol = db.Produto
    print("Produtos existentes: ")
    
    products = list(mycol.find())
    
    if not products:
        print("Nenhum produto encontrado.")
    else:
        for i, produto in enumerate(products, start=1):
            print(f"{i}. {produto['nome_produto']}")
    
    selected_id = input("Selecione um produto pelo ID para atualizar (ou pressione ENTER para sair): ")
    
    if selected_id:
        try:
            selected_id = int(selected_id)
            if 1 <= selected_id <= len(products):
                selected_product = products[selected_id - 1]
                print("Dados do produto:")
                print(f"Nome do Produto: {selected_product['nome_produto']}, Descrição: {selected_product['descricao']}, Data de Cadastro: {selected_product['data_cadastro']}")
                
                novo_nome = input("Mudar Nome do Produto: (Digite o novo nome ou pressione ENTER para manter o mesmo nome) ")
                if novo_nome:
                    selected_product['nome_produto'] = novo_nome

                nova_descricao = input("Mudar Descrição: (Digite a nova descrição ou pressione ENTER para manter a mesma descrição) ")
                if nova_descricao:
                    selected_product['descricao'] = nova_descricao

                newvalues = {"$set": selected_product}
                mycol.update_one({"_id": selected_product['_id']}, newvalues)
                print(f"Produto atualizado com sucesso!")
            else:
                print("ID inválido.")
        except ValueError:
            print("ID deve ser um número válido.")
    else:
        print("Saindo da atualização de produtos.")


def delete_produto():
    global db
    mycol = db.Produto
    print("Produtos existentes: ")
    
    products = list(mycol.find())
    
    if not products:
        print("Nenhum produto encontrado.")
    else:
        for i, produto in enumerate(products, start=1):
            print(f"{i}. {produto['nome_produto']}")
    
    selected_id = input("Selecione um produto pelo ID para excluir (ou pressione ENTER para sair): ")
    
    if selected_id:
        try:
            selected_id = int(selected_id)
            if 1 <= selected_id <= len(products):
                selected_product = products[selected_id - 1]
                mycol.delete_one({"_id": selected_product['_id']})
                print(f"Produto com ID {selected_id} foi removido com sucesso")
            else:
                print("ID inválido.")
        except ValueError:
            print("ID deve ser um número válido.")
    else:
        print("Saindo da exclusão de produtos.")