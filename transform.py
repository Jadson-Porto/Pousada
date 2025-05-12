import pandas as pd

def carregar_planilhas(arquivo):
    cliente = pd.read_excel(arquivo, sheet_name="cliente")
    quarto = pd.read_excel(arquivo, sheet_name="quarto")
    status = pd.read_excel(arquivo, sheet_name="status")
    data = pd.read_excel(arquivo, sheet_name="data")
    reserva = pd.read_excel(arquivo, sheet_name="reserva")
    return cliente, quarto, status, data, reserva

def tratar_cliente(df):
    df = df.dropna(subset=["Id", "Nome"])
    return df

def tratar_quarto(df):
    df["Preco"] = df["Preco"].fillna(0)
    return df

def tratar_status(df):
    df = df.dropna(subset=["Nome"])
    return df

def tratar_data(df):
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df = df.dropna(subset=["Data", "Nro_quarto", "Status"])
    return df

def tratar_reserva(df):
    df["Data_inicio_data"] = pd.to_datetime(df["Data_inicio_data"], errors="coerce")
    df["Data_fim_data"] = pd.to_datetime(df["Data_fim_data"], errors="coerce")
    df = df.dropna(subset=[
        "Nro", "Nome_status", "Data_inicio_data", "Numero_quarto_data_inicio",
        "Data_fim_data", "Nro_quarto_data_fim", "Data", "Id_cliente"
    ])
    return df
