from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 

uri = "" # Insira a url de sua base de dados

# Cria um novo cliente e conecta ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.Mercado_Livre

def add_vendedor():
    global db
    mycol = db.Vendedor
    print("\nInserindo um novo vendedor")
    nome_vendedor = input("Nome do Vendedor: ")
    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    vendedor = {
        "nome_vendedor": nome_vendedor,
        "data_cadastro": data_cadastro
    }

    x = mycol.insert_one(vendedor)
    print("Vendedor inserido com ID ", x.inserted_id)

def read_vendedor(nome_vendedor):
    global db
    mycol = db.Vendedor
    print("Vendedores existentes: ")
    if not len(nome_vendedor):
        mydoc = mycol.find()
        for vendedor in mydoc:
            print(f" {vendedor['nome_vendedor']}")
    else:
        myquery = {"nome_vendedor": nome_vendedor}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(f"Vendedor: {x['nome_vendedor']}, Data de Cadastro: {x['data_cadastro']}")

def update_vendedor(nome_vendedor):
    global db
    mycol = db.Vendedor
    myquery = {"nome_vendedor": nome_vendedor}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        print("Dados do vendedor:")
        print(f"{mydoc['nome_vendedor']}, Data de Cadastro: {mydoc['data_cadastro']}")

        novo_nome = input("Mudar Nome do Vendedor: (Digite o novo nome ou pressione ENTER para manter o mesmo nome) ")
        if novo_nome:
            mydoc['nome_vendedor'] = novo_nome

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print(f"Vendedor atualizado com sucesso!")

    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado")

def delete_vendedor(nome_vendedor):
    global db
    mycol = db.Vendedor
    myquery = {"nome_vendedor": nome_vendedor}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        mycol.delete_one(myquery)
        print(f"Vendedor com o nome '{nome_vendedor}' foi removido com sucesso")
    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado")

def cadastro_produto():
    global db
    mycol_produto = db.Produto
    mycol_vendedor = db.Vendedor

    print("Produtos existentes: ")
    produtos = list(mycol_produto.find())
    for i, produto in enumerate(produtos, 1):
        print(f"{i}.  {produto['nome_produto']}")

    while True:
        try:
            produto_id = int(input("Selecione um produto (digite o ID): "))
            if 1 <= produto_id <= len(produtos):
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

    produto_selecionado = produtos[produto_id - 1]

    nome_vendedor = input("Digite o nome do vendedor: ")

    vendedor = mycol_vendedor.find_one({"nome_vendedor": nome_vendedor})

    if vendedor:
        preco = float(input("Digite o preço do produto: "))
        quantidade_disponivel = int(input("Digite a quantidade disponível: "))

        produto_vendedor = {
            "nome_produto": produto_selecionado["nome_produto"],
            "descricao": produto_selecionado["descricao"],
            "preco": preco,
            "quantidade_disponivel": quantidade_disponivel
        }
        if "produtos" not in vendedor:
            vendedor["produtos"] = [produto_vendedor]
        else:
            vendedor["produtos"].append(produto_vendedor)

        newvalues = {"$set": vendedor}
        mycol_vendedor.update_one({"_id": vendedor["_id"]}, newvalues)

        print(f"Produto '{produto_selecionado['nome_produto']}' adicionado ao vendedor '{nome_vendedor}' com sucesso.")
    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado.")



def listar_produtos(nome_vendedor):
    global db
    mycol_vendedor = db.Vendedor

    vendedor = mycol_vendedor.find_one({"nome_vendedor": nome_vendedor})

    if vendedor:
        print(f"Produtos do vendedor '{nome_vendedor}':")
        if "produtos" in vendedor and vendedor["produtos"]:
            for produto in vendedor["produtos"]:
                print(f"{produto['nome_produto']}, Descrição: {produto['descricao']} , Preço: R$ {produto['preco']}, Quantidade disponível: {produto['quantidade_disponivel']}")
        else:
            print("O vendedor não possui produtos cadastrados.")
    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado.")

def atualizar_produto():
    global db
    mycol_vendedor = db.Vendedor

    nome_vendedor = input("Digite o nome do vendedor: ")

    
    vendedor = mycol_vendedor.find_one({"nome_vendedor": nome_vendedor})

    if vendedor:
        if "produtos" in vendedor and len(vendedor["produtos"]) > 0:
            print(f"Produtos do vendedor '{nome_vendedor}':")
            for i, produto in enumerate(vendedor["produtos"], 1):
                print(f"{i}.  {produto['nome_produto']}, Descrição: {produto['descricao']}")

            
            while True:
                try:
                    produto_id = int(input("Selecione um produto (digite o ID): "))
                    if 1 <= produto_id <= len(vendedor["produtos"]):
                        break
                    else:
                        print("ID inválido. Tente novamente.")
                except ValueError:
                    print("ID inválido. Tente novamente.")

           
            produto_selecionado = vendedor["produtos"][produto_id - 1]

            novo_preco = float(input("Digite o novo preço do produto: "))
            nova_quantidade = int(input("Digite a nova quantidade disponível: "))

            
            vendedor["produtos"][produto_id - 1]["preco"] = novo_preco
            vendedor["produtos"][produto_id - 1]["quantidade_disponivel"] = nova_quantidade

            
            mycol_vendedor.update_one({"_id": vendedor["_id"]}, {"$set": vendedor})

            print(f"Produto '{produto_selecionado['nome_produto']}' atualizado com sucesso.")
        else:
            print("O vendedor não possui produtos cadastrados.")
    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado.")

def remover_produto():
    global db
    mycol_vendedor = db.Vendedor

    nome_vendedor = input("Digite o nome do vendedor: ")

    vendedor = mycol_vendedor.find_one({"nome_vendedor": nome_vendedor})

    if vendedor:
        if "produtos" in vendedor and len(vendedor["produtos"]) > 0:
            print(f"Produtos do vendedor '{nome_vendedor}':")
            for i, produto in enumerate(vendedor["produtos"], 1):
                print(f"{i}.  {produto['nome_produto']}, Descrição: {produto['descricao']}")

            while True:
                try:
                    produto_id = int(input("Selecione um produto para remoção (digite o ID): "))
                    if 1 <= produto_id <= len(vendedor["produtos"]):
                        break
                    else:
                        print("ID inválido. Tente novamente.")
                except ValueError:
                    print("ID inválido. Tente novamente.")

            produto_selecionado = vendedor["produtos"].pop(produto_id - 1)

            mycol_vendedor.update_one({"_id": vendedor["_id"]}, {"$set": vendedor})

            print(f"Produto '{produto_selecionado['nome_produto']}' removido com sucesso.")
        else:
            print("O vendedor não possui produtos cadastrados.")
    else:
        print(f"Vendedor com o nome '{nome_vendedor}' não encontrado.")