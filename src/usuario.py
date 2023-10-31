from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 
import uri

uriMongo = uri.get_db_connection()
# Cria um novo cliente e conecta ao servidor
client = MongoClient(uriMongo, server_api=ServerApi('1'))
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
            nome = mydoc.get("nome", "Nome não disponível")
            sobrenome = mydoc.get("sobrenome", "Sobrenome não disponível")
            cpf = mydoc.get("cpf", "CPF não disponível")
            end = mydoc.get("end", "Endereço não disponível")
            favoritos = mydoc.get("favoritos")
            compra = mydoc.get("compra")
            
            print(f"Nome: {nome} {sobrenome}, CPF: {cpf}, Endereço: {end}")
            
            if favoritos is None:
                print("Não possui favoritos")
            elif favoritos:
                print(f"Favoritos: {favoritos}")
            
            if compra is None:
                print("Não possui compras")
            elif compra:
                print(f"Compras: {compra}")
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
    
def get_lista_produtos():
    global db
    produto_col = db.Produto
    produtos = produto_col.find()
    lista_produtos = [produto["nome_produto"] for produto in produtos]
    return lista_produtos

def add_favorito(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        lista_produtos = get_lista_produtos()

        if lista_produtos:
            print("Produtos disponíveis:")
            for i, produto in enumerate(lista_produtos, 1):
                print(f"{i}. {produto}")

            produto_idx = input("Digite o número do produto que deseja adicionar aos favoritos: ")

            try:
                produto_idx = int(produto_idx)
                if 1 <= produto_idx <= len(lista_produtos):
                    produto = lista_produtos[produto_idx - 1]
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
                    print("Número de produto inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite o número do produto.")
        else:
            print("Não há produtos disponíveis.")
    else:
        print(f"Usuário com CPF {cpf} não encontrado")



def delete_favorito(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        if "favoritos" in mydoc and mydoc["favoritos"]:
            print("Produtos nos favoritos do usuário:")
            for i, favorito in enumerate(mydoc["favoritos"], 1):
                print(f"{i}. {favorito['produto']}")

            produto_idx = input("Digite o número do produto que deseja remover dos favoritos: ")

            try:
                produto_idx = int(produto_idx)
                if 1 <= produto_idx <= len(mydoc["favoritos"]):
                    produto = mydoc["favoritos"][produto_idx - 1]["produto"]
                    mydoc["favoritos"].pop(produto_idx - 1) 
                    newvalues = {"$set": mydoc}
                    mycol.update_one(myquery, newvalues)
                    print(f"Produto '{produto}' removido dos favoritos do usuário com CPF {cpf}")
                else:
                    print("Número de produto inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite o número do produto.")
        else:
            print("O usuário não possui produtos nos favoritos.")
    else:
        print(f"Usuário com CPF {cpf} não encontrado")


def listar_produtos_e_vendedores():
    global db
    produto_col = db.Produto
    vendedor_col = db.Vendedor

    produtos = list(produto_col.find())
    
    if not produtos:
        print("Não há produtos disponíveis.")
        return None, None

    print("Produtos disponíveis:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome_produto']}")

    produto_idx = input("Digite o número do produto que deseja adicionar à compra: ")

    try:
        produto_idx = int(produto_idx)
        if 1 <= produto_idx <= len(produtos):
            produto_selecionado = produtos[produto_idx - 1]
            print(f"Produto selecionado: {produto_selecionado['nome_produto']}")
        else:
            print("Número de produto inválido.")
            return None, None
    except ValueError:
        print("Entrada inválida. Por favor, digite o número do produto.")
        return None, None

    vendedores_disponiveis = []

    vendedor_idx = 1

    print("Vendedores disponíveis para o produto:")
    vendedor_idx_mapping = {}  
    for vendedor in vendedor_col.find():
        for produto in vendedor.get("produtos", []):
            if produto.get("nome_produto") == produto_selecionado["nome_produto"]:
                vendedores_disponiveis.append(vendedor)
                print(f"{vendedor_idx}. {vendedor['nome_vendedor']}")
                vendedor_idx_mapping[vendedor_idx] = vendedor
                vendedor_idx += 1

    if not vendedores_disponiveis:
        print("Este produto não possui vendedores disponíveis.")
        return None, None

    vendedor_idx = input("Digite o número do vendedor desejado: ")

    try:
        vendedor_idx = int(vendedor_idx)
        if vendedor_idx in vendedor_idx_mapping:
            vendedor_selecionado = vendedor_idx_mapping[vendedor_idx]
            print(f"Vendedor selecionado: {vendedor_selecionado['nome_vendedor']}")
        else:
            print("Número de vendedor inválido.")
            return None, None
    except ValueError:
        print("Entrada inválida. Por favor, digite o número do vendedor.")
        return None, None

    return produto_selecionado, vendedor_selecionado



def add_compra(cpf):
    global db
    mycol = db.Usuário
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)

    if mydoc:
        compras = mydoc.get("compra", [])

        totalCompra = 0  # Inicializa o total da compra

        compra_atual = {"produtos": []}

        while True:
            produto_selecionado, vendedor_selecionado = listar_produtos_e_vendedores()

            if produto_selecionado and vendedor_selecionado:
                nomeProduto = produto_selecionado["nome_produto"]
                vendedor_produtos = vendedor_selecionado.get("produtos", [])
                
                # Encontre o preço do produto no vendedor
                for produto_vendedor in vendedor_produtos:
                    if produto_vendedor.get("nome_produto") == nomeProduto:
                        precoUnitario = produto_vendedor.get("preco", 0)
                        break
                else:
                    precoUnitario = 0

                quantidade = int(input("Digite a quantidade: "))
                subTotal = precoUnitario * quantidade
                descricaoProduto = produto_selecionado.get("descricao", "")
                vendedor = vendedor_selecionado["nome_vendedor"]

                produto = {
                    "nomeProduto": nomeProduto,
                    "precoUnitario": precoUnitario,
                    "quantidade": quantidade,
                    "subTotal": subTotal,
                    "descricaoProduto": descricaoProduto,
                    "vendedor": vendedor
                }

                compra_atual["produtos"].append(produto)

                totalCompra += subTotal  # Adiciona o subTotal ao total da compra

                print(f"Produto '{nomeProduto}' adicionado à compra do usuário com CPF {cpf}")

                continuar = input("Deseja adicionar outro produto à compra (S/N)? ")
                if continuar.lower() != 's':
                    break

        # Atualiza o total da compra na compra atual
        compra_atual["totalCompra"] = totalCompra

        compras.append(compra_atual)

        mydoc["compra"] = compras
        newvalues = {"$set": mydoc}
        mycol.update_one(myquery, newvalues)
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
            