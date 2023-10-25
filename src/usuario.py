from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 

uri = "" # Insira a url de sua base de dados

# Cria um novo cliente e conecta ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.Mercado_Livre

def delete_usuario(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf" : cpf}
    mydoc = mycol.delete_one(myquery)

    if mydoc.deleted_count == 0:
        print(f"Usuário com o CPF {cpf} não encontrado")
    else:
        print(f"Usuário com o CPF {cpf} deletado com sucesso")


def create_usuario():
    global db
    mycol = db.Usuário
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    end = []
    while (key != 'N' and key !='n'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {        
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_usuario(cpf):
    global db
    mycol = db.Usuário
    print("Usuários existentes: ")
    if not len(cpf):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(f"Nome: {x["nome"]} CPF: {x["cpf"]}")
    else:
        myquery = {"cpf": cpf}
        mydoc = mycol.find_one(myquery)
        if mydoc:
            print(f"Nome: {mydoc["nome"]} {mydoc["sobrenome"]}, CPF: {mydoc["cpf"]}, Endereço: {mydoc["end"]}, Favoritos: {mydoc["favoritos"]}, Compras: {mydoc["compra"]}")
        else:
           print(f"Usuário com CPF {cpf} não encontrado") 

def update_usuario(cpf):
    global db
    key = 1
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)
    if mydoc is None:
        print(f"Usuário com CPF {cpf} não encontrado")  
    else:
        print("Dados do usuário: ",mydoc)
        nome = input("Mudar Nome: (Digite o nome ou clique ENTER para manter o mesmo nome) ")
        if len(nome):
            mydoc["nome"] = nome

        sobrenome = input("Mudar Sobrenome: (Digite o sobrenome ou clique ENTER para manter o mesmo sobrenome)")
        if len(sobrenome):
            mydoc["sobrenome"] = sobrenome

        cpf = input("Mudar CPF: (Digite o CPF ou clique ENTER para manter o mesmo CPF)")
        if len(cpf):
            mydoc["cpf"] = cpf

        end = input("Mudar endereço: (Digite  S para atualizar ou clique ENTER para manter o mesmo endereço)")
        if len(end):
            end = []
            while (key != 'N' and key !='n'):
                rua = input("Rua: ")
                num = input("Num: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                cep = input("CEP: ")
                endereco = {        
                    "rua":rua,
                    "num": num,
                    "bairro": bairro,
                    "cidade": cidade,
                    "estado": estado,
                    "cep": cep
                }
                end.append(endereco)
                key = input("Deseja cadastrar um novo endereço (S/N)? ")
            mydoc["end"] = end 
        newvalues = { "$set": mydoc }
        mycol.update_one(myquery, newvalues)

def add_favorito(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        produto = input("Digite o nome do produto que deseja adicionar aos favoritos: ")
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        favorito = {"produto": produto, "data": data}
        
        if "favoritos" in mydoc:
            mydoc["favoritos"].append(favorito)
        else:
            mydoc["favoritos"] = [favorito]

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print(f"Produto '{produto}' adicionado aos favoritos do usuário com CPF {cpf}")
    else:
        print(f"Usuário com CPF {cpf} não encontrado")


def delete_favorito(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        produto = input("Digite o nome do produto que deseja remover dos favoritos: ")
        if "favoritos" in mydoc:
            for x in mydoc["favoritos"]:
                if x["produto"] == produto:
                    mydoc["favoritos"].remove(x)
                    newvalues = {"$set": mydoc}
                    mycol.update_one(myquery, newvalues)
                    print(f"Produto '{produto}' removido dos favoritos do usuário com CPF {cpf}")
        else:
            print(f"Usuário com CPF {cpf} não encontrado")

def add_compra(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        nomeProduto = input("Digite o nome do produto: ")
        precoUnitario = float(input("Digite o preço unitário: "))
        quantidade = int(input("Digite a quantidade: "))
        subTotal = precoUnitario * quantidade
        descricaoProduto = input("Digite a descrição do produto: ")
        vendedor = input("Digite o nome do vendedor: ")
        totalCompra = subTotal
        dataCompra = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        compra = {
            "produto": {
                "nomeProduto": nomeProduto,
                "precoUnitario": precoUnitario,
                "quantidade": quantidade,
                "subTotal": subTotal,
                "descricaoProduto": descricaoProduto,
                "vendedor": vendedor
            },
            "totalCompra": totalCompra,
            "dataCompra": dataCompra
        }

        if "compra" in mydoc:
            mydoc["compra"].append(compra)
        else:
            mydoc["compra"] = [compra]

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print(f"Compra adicionada para o usuário com CPF {cpf}")
    else:
        print(f"Usuário com CPF {cpf} não encontrado")

def add_compra(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        nomeProduto = input("Digite o nome do produto: ")
        precoUnitario = float(input("Digite o preço unitário: "))
        quantidade = int(input("Digite a quantidade: "))
        subTotal = precoUnitario * quantidade
        descricaoProduto = input("Digite a descrição do produto: ")
        vendedor = input("Digite o nome do vendedor: ")
        totalCompra = subTotal
        dataCompra = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        compra = {
            "produto": {
                "nomeProduto": nomeProduto,
                "precoUnitario": precoUnitario,
                "quantidade": quantidade,
                "subTotal": subTotal,
                "descricaoProduto": descricaoProduto,
                "vendedor": vendedor
            },
            "totalCompra": totalCompra,
            "dataCompra": dataCompra
        }

        if "compra" in mydoc:
            mydoc["compra"].append(compra)
        else:
            mydoc["compra"] = [compra]

        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
        print(f"Compra adicionada para o usuário com CPF {cpf}")
    else:
        print(f"Usuário com CPF {cpf} não encontrado")

def delete_compra(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        nomeProduto = input("Digite o nome do produto: ")
        if "compra" in mydoc:
            for x in mydoc["compra"]:
                if x["produto"]["nomeProduto"] == nomeProduto:
                    mydoc["compra"].remove(x)
                    newvalues = {"$set": mydoc}
                    mycol.update_one(myquery, newvalues)
                    print(f"Compra removida do usuário com CPF {cpf}")
        else:
            print(f"Usuário com CPF {cpf} não encontrado")
            