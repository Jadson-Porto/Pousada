# %%
# imports
import os
import pyodbc
import pandas as pd

from dotenv import load_dotenv

from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "nome do arquivo de origem"
destino = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=ETL_VITOR;"
    "UID=sa2;"
    "PWD=sa;"
)

cnxn = pyodbc.connect(conn_str)

    # SQL query
query = "SELECT TOP 10 * FROM Cliente"

    # Execute query and load into DataFrame
df = pd.read_sql_query(query, cnxn)
print(df.head())

etl = ETL(origem, destino)

etl.extract()
etl.transform()
etl.load()