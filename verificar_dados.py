import pyodbc
import pandas as pd

conn = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=localhost;"
    r"Database=HotelDB;"
    r"Trusted_Connection=yes;"
)

tabelas = ["Cliente", "Quarto", "Status", "Data", "Reserva"]

for tabela in tabelas:
    print(f"\n🔎 Tabela: {tabela}")
    df = pd.read_sql(f"SELECT * FROM {tabela}", conn)
    print(df)

conn.close()