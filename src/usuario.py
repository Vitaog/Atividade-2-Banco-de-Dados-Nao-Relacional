from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime 
import uri

uriMongo = uri.get_db_connection()
# Cria um novo cliente e conecta ao servidor
client = MongoClient(uriMongo, server_api=ServerApi('1'))
global db
db = client.Mercado_Livre

def delete_usuario():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}  
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário que deseja deletar (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    mycol.delete_one({"cpf": cpf})
    print(f"Usuário com CPF {cpf} deletado com sucesso.")


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

def read_usuario():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário que deseja visualizar (ou deixe em branco para sair): ")
    
    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    nome = mydoc.get("nome", "Nome não disponível")
    sobrenome = mydoc.get("sobrenome", "Sobrenome não disponível")
    cpf = mydoc.get("cpf", "CPF não disponível")
    end = mydoc.get("end", "Endereço não disponível")
    favoritos = mydoc.get("favoritos")
    compra = mydoc.get("compra")

    print(f"Nome: {nome} {sobrenome}")
    print(f"CPF: {cpf}")
    print()

    if end != "Endereço não disponível":
        print("Endereço:")
        for endereco in end:
            print(f"Rua: {endereco['rua']}, Número: {endereco['num']}, Bairro: {endereco['bairro']}, Cidade: {endereco['cidade']}, Estado: {endereco['estado']}, CEP: {endereco['cep']}")
            print()

    if favoritos is None:
        print("Não possui favoritos")
    elif favoritos:
        print("Favoritos:")
        for fav in favoritos:
            print(f"Produto: {fav['produto']}, Preço: {fav['preco']}, Vendedor: {fav['vendedor']}, Data: {fav['data']}")
            print()

    if compra is None:
        print("Não possui compras")
    elif compra:
        print("Compras:")
        for compra_info in compra:
            print("Produtos da Compra:")
            for produto_compra in compra_info['produtos']:
                print(f"Nome do Produto:{produto_compra['nomeProduto']}, Preço Unitário: {produto_compra['precoUnitario']}, Quantidade: {produto_compra['quantidade']}, Subtotal: {produto_compra['subTotal']}, Descrição: {produto_compra['descricaoProduto']}, Vendedor: {produto_compra['vendedor']}")
            print(f"Total da compra: {compra_info['totalCompra']}")
            print(f"Data da Compra: {compra_info['dataCompra']}")
            print()

def update_usuario():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário que deseja atualizar (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    print("Dados atuais do usuário:")
    nome = mydoc.get("nome", "Nome não disponível")
    sobrenome = mydoc.get("sobrenome", "Sobrenome não disponível")
    cpf = mydoc.get("cpf", "CPF não disponível")
    end = mydoc.get("end", "Endereço não disponível")
    favoritos = mydoc.get("favoritos")
    compra = mydoc.get("compra")

    print(f"Nome: {nome} {sobrenome}, CPF: {cpf}")
    for endereco in end:
        print(f"Rua: {endereco['rua']}, Número: {endereco['num']}, Bairro: {endereco['bairro']}, Cidade: {endereco['cidade']}, Estado: {endereco['estado']}, CEP: {endereco['cep']}")

    if favoritos is None:
        print("Não possui favoritos")
    elif favoritos:
        print(f"Favoritos: {favoritos}")

    if compra is None:
        print("Não possui compras")
    elif compra:
        print(f"Compras: {compra}")

    key = 1
    nome = input("Mudar Nome: (Digite o nome ou clique ENTER para manter o mesmo nome) ")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome: (Digite o sobrenome ou clique ENTER para manter o mesmo sobrenome)")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    new_cpf = input("Mudar CPF: (Digite o CPF ou clique ENTER para manter o mesmo CPF)")
    if len(new_cpf):
        mydoc["cpf"] = new_cpf

    end = input("Mudar endereço: (Digite S para atualizar ou clique ENTER para manter o mesmo endereço)")
    if len(end):
        end = []
        while (key != 'N' and key != 'n'):
            rua = input("Rua: ")
            num = input("Num: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")
            cep = input("CEP: ")
            endereco = {
                "rua": rua,
                "num": num,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
            end.append(endereco)
            key = input("Deseja cadastrar um novo endereço (S/N)? ")
        mydoc["end"] = end

    mycol.update_one({"cpf": cpf}, {"$set": mydoc})
    print("Usuário atualizado com sucesso.")

def get_lista_produtos():
    global db
    produto_col = db.Produto
    produtos = produto_col.find()
    lista_produtos = [produto["nome_produto"] for produto in produtos]
    return lista_produtos

def add_favorito():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário ao qual deseja adicionar um favorito (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

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

                vendedores_col = db.Vendedor
                produto_col = db.Produto

                produto_info = produto_col.find_one({"nome_produto": produto})
                if produto_info:
                    nome_produto = produto_info["nome_produto"]
                    descricao = produto_info["descricao"]

                    vendedores_com_produto = []
                    for vendedor in vendedores_col.find():
                        for prod in vendedor.get("produtos", []):
                            if prod.get("nome_produto") == nome_produto and prod.get("descricao") == descricao:
                                preco = prod.get("preco")
                                vendedores_com_produto.append((vendedor, preco))

                    if vendedores_com_produto:
                        print("Vendedores com este produto:")
                        for i, (vendedor, preco) in enumerate(vendedores_com_produto, 1):
                            print(f"{i}. {vendedor['nome_vendedor']}, Preço: R$ {preco:.2f}")

                        vendedor_idx = input("Digite o número do vendedor que deseja selecionar: ")

                        try:
                            vendedor_idx = int(vendedor_idx)
                            if 1 <= vendedor_idx <= len(vendedores_com_produto):
                                vendedor_selecionado, preco = vendedores_com_produto[vendedor_idx - 1]
                                data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                                myquery = {"cpf": cpf}
                                mydoc = mycol.find_one(myquery)

                                if mydoc:
                                    if "favoritos" in mydoc:
                                        mydoc["favoritos"].append({
                                            "produto": nome_produto,
                                            "preco": preco,
                                            "vendedor": vendedor_selecionado["nome_vendedor"],
                                            "data": data
                                        })
                                    else:
                                        mydoc["favoritos"] = [{
                                            "produto": nome_produto,
                                            "preco": preco,
                                            "vendedor": vendedor_selecionado["nome_vendedor"],
                                            "data": data
                                        }]

                                    newvalues = {"$set": mydoc}
                                    mycol.update_one(myquery, newvalues)

                                    print(f"Produto '{nome_produto}' adicionado aos favoritos do usuário com CPF {cpf}.")
                                    print(f"Selecionou o vendedor: {vendedor_selecionado['nome_vendedor']}")
                                    print(f"Preço do produto: R$ {preco:.2f}")
                                else:
                                    print(f"Usuário com CPF {cpf} não encontrado.")
                            else:
                                print("Número de vendedor inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, digite o número do vendedor.")
                    else:
                        print("Nenhum vendedor cadastrou este produto.")
                else:
                    print(f"Produto com nome {produto} não encontrado.")
            else:
                print("Número de produto inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite o número do produto.")
    else:
        print("Não há produtos disponíveis.")

def delete_favorito():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário do qual deseja remover um favorito (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    if "favoritos" in mydoc and mydoc["favoritos"]:
        print("Favoritos do usuário:")
        for i, favorito in enumerate(mydoc["favoritos"], 1):
            print(f"{i}. {favorito['produto']} (Vendedor: {favorito['vendedor']}, Preço: R$ {favorito['preco']:.2f})")

        favorito_idx = input("Digite o número do favorito que deseja remover: ")

        try:
            favorito_idx = int(favorito_idx)
            if 1 <= favorito_idx <= len(mydoc["favoritos"]):
                removed_favorito = mydoc["favoritos"].pop(favorito_idx - 1)
                newvalues = {"$set": mydoc}
                mycol.update_one({"cpf": cpf}, newvalues)

                print(f"Favorito removido com sucesso:")
                print(f"Produto: {removed_favorito['produto']}")
                print(f"Vendedor: {removed_favorito['vendedor']}")
                print(f"Preço: R$ {removed_favorito['preco']:.2f}")
            else:
                print("Número de favorito inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite o número do favorito.")
    else:
        print("O usuário não possui favoritos cadastrados.")

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

    vendedor_idx_mapping = {}
    for vendedor in vendedor_col.find():
        for produto in vendedor.get("produtos", []):
            if produto.get("nome_produto") == produto_selecionado["nome_produto"]:
                preco = produto.get("preco", 0)
                vendedores_disponiveis.append((vendedor, preco))
                vendedor_idx_mapping[len(vendedores_disponiveis)] = (vendedor, preco)

    if not vendedores_disponiveis:
        print("Este produto não possui vendedores disponíveis.")
        return None, None

    print("Vendedores disponíveis para o produto:")
    for i, (vendedor, preco) in enumerate(vendedores_disponiveis, 1):
        print(f"{i}. {vendedor['nome_vendedor']} - Preço: R$ {preco:.2f}")

    vendedor_idx = input("Digite o número do vendedor desejado: ")

    try:
        vendedor_idx = int(vendedor_idx)
        if 1 <= vendedor_idx <= len(vendedores_disponiveis):
            vendedor_selecionado, preco = vendedor_idx_mapping[vendedor_idx]
            print(f"Vendedor selecionado: {vendedor_selecionado['nome_vendedor']}")
            print(f"Preço do produto: R$ {preco:.2f}")
        else:
            print("Número de vendedor inválido.")
            return None, None
    except ValueError:
        print("Entrada inválida. Por favor, digite o número do vendedor.")
        return None, None

    return produto_selecionado, vendedor_selecionado


def add_compra():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário ao qual deseja adicionar uma compra (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    compras = mydoc.get("compra", [])
    totalCompra = 0
    compra_atual = {"produtos": []}

    while True:
        produto_selecionado, vendedor_selecionado = listar_produtos_e_vendedores()

        if produto_selecionado and vendedor_selecionado:
            nomeProduto = produto_selecionado["nome_produto"]
            vendedor_produtos = vendedor_selecionado.get("produtos", [])

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
            totalCompra += subTotal

            print(f"Produto '{nomeProduto}' adicionado à compra do usuário com CPF {cpf}")

            continuar = input("Deseja adicionar outro produto à compra (S/N)? ")
            if continuar.lower() != 's':
                break

    compra_atual["totalCompra"] = totalCompra
    compra_atual["dataCompra"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    compras.append(compra_atual)

    mydoc["compra"] = compras
    newvalues = {"$set": mydoc}
    mycol.update_one({"cpf": cpf}, newvalues)

def delete_compra():
    global db
    mycol = db.Usuário

    cursor = mycol.find()
    user_dict = {}
    
    for user in cursor:
        print(f"Nome: {user['nome']} CPF: {user['cpf']}")
        user_dict[user['cpf']] = user

    if not user_dict:
        print("Não há nenhum usuário cadastrado no Mercado Livre.")
        return

    cpf = input("Digite o CPF do usuário do qual deseja remover uma compra (ou deixe em branco para sair): ")

    if not cpf:
        return

    if cpf not in user_dict:
        print(f"Usuário com CPF {cpf} não encontrado")
        return

    mydoc = user_dict[cpf]

    if "compra" in mydoc and mydoc["compra"]:
        while True:
            print("Compras do usuário:")
            for i, compra in enumerate(mydoc["compra"], 1):
                print(f"{i}. Total da compra: R$ {compra['totalCompra']:.2f}")
                print("Produtos da Compra:")
                for produto_compra in compra["produtos"]:
                    print(f"Nome do Produto: {produto_compra['nomeProduto']}")
                    print(f"Nome do Vendedor: {produto_compra['vendedor']}")
                print()

            compra_idx = input("Digite o número da compra que deseja excluir (ou 'V' para voltar): ")

            if compra_idx.lower() == 'v':
                break

            try:
                compra_idx = int(compra_idx)
                if 1 <= compra_idx <= len(mydoc["compra"]):
                    removed_compra = mydoc["compra"].pop(compra_idx - 1)
                    newvalues = {"$set": mydoc}
                    mycol.update_one({"cpf": cpf}, newvalues)

                    print(f"Compra removida com sucesso:")
                    print(f"Total da compra: R$ {removed_compra['totalCompra']:.2f}")
                    for produto_compra in removed_compra["produtos"]:
                        print(f"Nome do Produto: {produto_compra['nomeProduto']}")
                        print(f"Nome do Vendedor: {produto_compra['vendedor']}")
                else:
                    print("Número de compra inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite o número da compra.")
            else:
                break  
    else:
        print("O usuário não possui compras registradas.")
