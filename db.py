import pyodbc

def criar_conexao():
    try:
        conn = pyodbc.connect(
            r"Driver={SQL Server};"
            r"Server=TREINOPYTHON;"
            r"Database=HotelDB;"
            r"Trusted_Connection=yes;"
        )
        print("Conexão estabelecida com sucesso.")
        return conn
    except Exception as e:
        print(f"Erro na conexão com SQL Server: {e}")
        return None
    
