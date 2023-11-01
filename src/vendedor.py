from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 
import uri

uriMongo = uri.get_db_connection()
# Cria um novo cliente e conecta ao servidor
client = MongoClient(uriMongo, server_api=ServerApi('1'))
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

def listar_vendedores():
    global db
    mycol = db.Vendedor
    print("Vendedores existentes: ")
    mydoc = mycol.find()
    vendedores = list(mydoc)
    
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor['nome_vendedor']}, Avaliação: {vendedor.get('avaliacao_final', 'Não tem avaliação')}")

    return vendedores

def read_vendedor():
    global db
    mycol = db.Vendedor
    vendedores = listar_vendedores()
    
    if not vendedores:
        print("Não existem vendedores cadastrados.")
        return
    
    while True:
        try:
            vendedor_id_input = input("Selecione um vendedor por ID (digite o ID) ou pressione Enter para voltar: ")
            if vendedor_id_input == "":
                break  
            vendedor_id = int(vendedor_id_input)
            if 1 <= vendedor_id <= len(vendedores):
                vendedor_selecionado = vendedores[vendedor_id - 1]
                print(f"Vendedor selecionado: {vendedor_selecionado['nome_vendedor']}, Avaliação: {vendedor_selecionado.get('avaliacao_final', 'Não tem avaliação')}")
                
                if "produtos" in vendedor_selecionado:
                    print("Produtos do vendedor:")
                    for produto in vendedor_selecionado["produtos"]:
                        print(f"Nome do Produto: {produto['nome_produto']}, Descrição: {produto['descricao']}, Preço: R$ {produto['preco']}, Quantidade disponível: {produto['quantidade_disponivel']}")
                else:
                    print("O vendedor não possui produtos cadastrados.")
                
                break
            elif vendedor_id == 0:
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

def update_vendedor():
    global db
    mycol = db.Vendedor

    vendedores = listar_vendedores()

    if not vendedores:
        print("Não existem vendedores cadastrados.")
        return

    while True:
        try:
            vendedor_id_input = input("Selecione um vendedor por ID (digite o ID) ou pressione Enter para voltar: ")
            
            if not vendedor_id_input:
                return  

            vendedor_id = int(vendedor_id_input)

            if 1 <= vendedor_id <= len(vendedores):
                vendedor_selecionado = vendedores[vendedor_id - 1]
                nome_vendedor = vendedor_selecionado["nome_vendedor"]
                print(f"Vendedor selecionado: {nome_vendedor}")

                novo_nome = input("Mudar Nome do Vendedor: (Digite o novo nome ou pressione ENTER para manter o mesmo nome) ")
                if novo_nome:
                    vendedor_selecionado['nome_vendedor'] = novo_nome

                newvalues = {"$set": vendedor_selecionado}
                mycol.update_one({"_id": vendedor_selecionado["_id"]}, newvalues)
                print(f"Vendedor '{nome_vendedor}' atualizado com sucesso!")
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

def delete_vendedor():
    global db
    mycol = db.Vendedor

    vendedores = listar_vendedores()

    if not vendedores:
        print("Não existem vendedores cadastrados.")
        return

    while True:
        try:
            vendedor_id_input = input("Selecione um vendedor por ID (digite o ID) ou pressione Enter para voltar: ")
            
            if not vendedor_id_input:
                return  

            vendedor_id = int(vendedor_id_input)

            if 1 <= vendedor_id <= len(vendedores):
                vendedor_selecionado = vendedores[vendedor_id - 1]
                nome_vendedor = vendedor_selecionado["nome_vendedor"]
                print(f"Vendedor selecionado: {nome_vendedor}")

                confirma = input(f"Tem certeza de que deseja remover o vendedor '{nome_vendedor}'? (S/N): ")
                if confirma.lower() == "s":
                    mycol.delete_one({"_id": vendedor_selecionado["_id"]})
                    print(f"Vendedor '{nome_vendedor}' removido com sucesso.")
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

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

    
    vendedores = list(mycol_vendedor.find())
    print("Vendedores disponíveis: ")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor['nome_vendedor']}")

    while True:
        try:
            vendedor_id = int(input("Selecione um vendedor (digite o ID): "))
            if 1 <= vendedor_id <= len(vendedores):
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

    vendedor_selecionado = vendedores[vendedor_id - 1]

    preco = float(input("Digite o preço do produto: "))
    quantidade_disponivel = int(input("Digite a quantidade disponível: "))

    produto_vendedor = {
        "nome_produto": produto_selecionado["nome_produto"],
        "descricao": produto_selecionado["descricao"],
        "preco": preco,
        "quantidade_disponivel": quantidade_disponivel
    }
    if "produtos" not in vendedor_selecionado:
        vendedor_selecionado["produtos"] = [produto_vendedor]
    else:
        vendedor_selecionado["produtos"].append(produto_vendedor)

    newvalues = {"$set": vendedor_selecionado}
    mycol_vendedor.update_one({"_id": vendedor_selecionado["_id"]}, newvalues)

    print(f"Produto '{produto_selecionado['nome_produto']}' adicionado ao vendedor '{vendedor_selecionado['nome_vendedor']}' com sucesso.")

def atualizar_produto():
    global db
    mycol_vendedor = db.Vendedor

    vendedores = list(mycol_vendedor.find())
    print("Vendedores disponíveis: ")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor['nome_vendedor']}")

    while True:
        try:
            vendedor_id = int(input("Selecione um vendedor (digite o ID): "))
            if 1 <= vendedor_id <= len(vendedores):
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

    vendedor_selecionado = vendedores[vendedor_id - 1]

    if "produtos" in vendedor_selecionado and len(vendedor_selecionado["produtos"]) > 0:
        print(f"Produtos do vendedor '{vendedor_selecionado['nome_vendedor']}:")
        for i, produto in enumerate(vendedor_selecionado["produtos"], 1):
            print(f"{i}. {produto['nome_produto']}, Descrição: {produto['descricao']}")

        while True:
            try:
                produto_id = int(input("Selecione um produto (digite o ID): "))
                if 1 <= produto_id <= len(vendedor_selecionado["produtos"]):
                    break
                else:
                    print("ID inválido. Tente novamente.")
            except ValueError:
                print("ID inválido. Tente novamente.")

        produto_selecionado = vendedor_selecionado["produtos"][produto_id - 1]

        novo_preco = float(input("Digite o novo preço do produto: "))
        nova_quantidade = int(input("Digite a nova quantidade disponível: "))

        vendedor_selecionado["produtos"][produto_id - 1]["preco"] = novo_preco
        vendedor_selecionado["produtos"][produto_id - 1]["quantidade_disponivel"] = nova_quantidade

        mycol_vendedor.update_one({"_id": vendedor_selecionado["_id"]}, {"$set": vendedor_selecionado})

        print(f"Produto '{produto_selecionado['nome_produto']}' atualizado com sucesso.")
    else:
        print("O vendedor não possui produtos cadastrados.")

def remover_produto():
    global db
    mycol_vendedor = db.Vendedor

    vendedores = list(mycol_vendedor.find())
    print("Vendedores disponíveis: ")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor['nome_vendedor']}")

    while True:
        try:
            vendedor_id = int(input("Digite o ID do vendedor: "))
            if 1 <= vendedor_id <= len(vendedores):
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Tente novamente.")

    vendedor_selecionado = vendedores[vendedor_id - 1]

    if "produtos" in vendedor_selecionado and len(vendedor_selecionado["produtos"]) > 0:
        print(f"Produtos do vendedor '{vendedor_selecionado['nome_vendedor']}:")
        for i, produto in enumerate(vendedor_selecionado["produtos"], 1):
            print(f"{i}. {produto['nome_produto']}, Descrição: {produto['descricao']}")

        while True:
            try:
                produto_id = int(input("Selecione um produto para remoção (digite o ID): "))
                if 1 <= produto_id <= len(vendedor_selecionado["produtos"]):
                    break
                else:
                    print("ID inválido. Tente novamente.")
            except ValueError:
                print("ID inválido. Tente novamente.")

        produto_selecionado = vendedor_selecionado["produtos"].pop(produto_id - 1)

        mycol_vendedor.update_one({"_id": vendedor_selecionado["_id"]}, {"$set": vendedor_selecionado})

        print(f"Produto '{produto_selecionado['nome_produto']}' removido com sucesso.")
    else:
        print("O vendedor não possui produtos cadastrados.")


def adicionar_avaliacao():
    global db
    mycol_vendedor = db.Vendedor

    vendedores = list(mycol_vendedor.find())
    
    if not vendedores:
        print("Não existem vendedores cadastrados.")
        return

    print("Lista de vendedores:")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor['nome_vendedor']}")

    while True:
        try:
            vendedor_id = int(input("Selecione o vendedor (digite o número): "))
            if 1 <= vendedor_id <= len(vendedores):
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Número inválido. Tente novamente.")

    vendedor_selecionado = vendedores[vendedor_id - 1]
    nome_vendedor = vendedor_selecionado["nome_vendedor"]

    if "avaliacoes" not in vendedor_selecionado:
        vendedor_selecionado["avaliacoes"] = []

    try:
        nota_avaliacao = float(input("Digite a nota da avaliação (0 a 10): "))
        if 0 <= nota_avaliacao <= 10:
            vendedor_selecionado["avaliacoes"].append(nota_avaliacao)

            # Calcular a avaliação final (média das avaliações)
            avaliacao_final = sum(vendedor_selecionado["avaliacoes"]) / len(vendedor_selecionado["avaliacoes"])
            vendedor_selecionado["avaliacao_final"] = avaliacao_final

            newvalues = {"$set": vendedor_selecionado}
            mycol_vendedor.update_one({"_id": vendedor_selecionado["_id"]}, newvalues)

            print(f"Avaliação adicionada ao vendedor '{nome_vendedor}' com sucesso.")
            print(f"Avaliação Final: {avaliacao_final:.2f}")
        else:
            print("A nota da avaliação deve estar no intervalo de 0 a 10.")
    except ValueError:
        print("Nota de avaliação inválida. Deve ser um número entre 0 e 10.")
