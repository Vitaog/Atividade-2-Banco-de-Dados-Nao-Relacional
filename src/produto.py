from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 

url = "" # Insira a url de sua base de dados

# Cria um novo cliente e conecta ao servidor
client = MongoClient(url, server_api=ServerApi('1'))
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

def read_produto(nome):
    global db
    mycol = db.Produto
    print("Produtos existentes: ")
    if not len (nome):
        mydoc = mycol.find()
        for produto in mydoc:
            print(f" {produto['nome_produto']}")
    else:
        myquery = {"nome_produto": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(f"Produto: {x['nome_produto']}, Descrição: {x['descricao']}")

    

def update_produto(nome_produto):
    global db
    mycol = db.Produto
    myquery = {"nome_produto": nome_produto}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        print("Dados do produto:")
        print(f"Nome do Produto: {mydoc['nome_produto']}, Descrição: {mydoc['descricao']}, Data de Cadastro: {mydoc['data_cadastro']}")
        
        novo_nome = input("Mudar Nome do Produto: (Digite o novo nome ou pressione ENTER para manter o mesmo nome) ")
        if novo_nome:
            mydoc['nome_produto'] = novo_nome

        nova_descricao = input("Mudar Descrição: (Digite a nova descrição ou pressione ENTER para manter a mesma descrição) ")
        if nova_descricao:
            mydoc['descricao'] = nova_descricao

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print(f"Produto atualizado com sucesso!")

    else:
        print(f"Produto com o nome '{nome_produto}' não encontrado")

def delete_produto(nome_produto):
    global db
    mycol = db.Produto
    myquery = {"nome_produto": nome_produto}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        mycol.delete_one(myquery)
        print(f"Produto com o nome '{nome_produto}' foi removido com sucesso")
    else:
        print(f"Produto com o nome '{nome_produto}' não encontrado")