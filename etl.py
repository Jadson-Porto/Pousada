from transform import (
    carregar_planilhas,
    tratar_cliente, tratar_quarto, tratar_status, tratar_data, tratar_reserva
)
from db import criar_conexao

try:
    print("📥 Carregando e tratando dados...")

    # Caminho do arquivo Excel
    arquivo = "reservas_hotel.xlsx"

    # Carregar e tratar
    cliente, quarto, status, data, reserva = carregar_planilhas(arquivo)
    cliente = tratar_cliente(cliente)
    quarto = tratar_quarto(quarto)
    status = tratar_status(status)
    data = tratar_data(data)
    reserva = tratar_reserva(reserva)

    print("🔗 Conectando ao banco de dados...")
    conn = criar_conexao()
    cursor = conn.cursor()

    # Inserções
    for _, row in cliente.iterrows():
        cursor.execute("""
            INSERT INTO Cliente (Id, Nome, Telefone, Cpf)
            VALUES (?, ?, ?, ?)
        """, int(row['Id']), row['Nome'], row['Telefone'], row['Cpf'])

    for _, row in quarto.iterrows():
        cursor.execute("""
            INSERT INTO Quarto (Nro, Preco, Descricao)
            VALUES (?, ?, ?)
        """, int(row['Nro']), float(row['Preco']), row['Descricao'])

    for _, row in status.iterrows():
        cursor.execute("""
            INSERT INTO Status (Nome)
            VALUES (?)
        """, row['Nome'])

    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO Data (Data, Nro_quarto, Status)
            VALUES (?, ?, ?)
        """, row['Data'], int(row['Nro_quarto']), row['Status'])

    for _, row in reserva.iterrows():
        cursor.execute("""
            INSERT INTO Reserva (
                Nro, Nome_status, Data_inicio_data,
                Numero_quarto_data_inicio, Data_fim_data,
                Nro_quarto_data_fim, Data, Id_cliente
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, int(row['Nro']), row['Nome_status'], row['Data_inicio_data'],
             int(row['Numero_quarto_data_inicio']), row['Data_fim_data'],
             int(row['Nro_quarto_data_fim']), row['Data'], int(row['Id_cliente']))

    conn.commit()
    print("✅ ETL executado com sucesso. Dados inseridos no SQL Server!")

except Exception as e:
    print(f"❌ Erro no ETL: {e}")

finally:
    if 'conn' in locals():
        conn.close()
