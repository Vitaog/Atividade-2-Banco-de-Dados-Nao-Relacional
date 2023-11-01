
# Defina a URI do seu banco de dados MongoDB aqui
MONGO_URI = ""

# Crie uma função para obter a conexão com o banco de dados
def get_db_connection():
    try:
        db = MONGO_URI
        return db
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")
        return None