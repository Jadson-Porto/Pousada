import pandas as pd

# Novos dados de clientes
clientes = {
    'Id': [1, 2, 3, 4, 5, 6, 7],
    'Nome': ['Jailson Silva', 'Fernanda Lima', 'Rafael Costa', 'Juliana Souza', 'Paulo Mendes', 'Ana Oliveira', 'Marcos Pereira'],
    'Telefone': ['999111222', '998222333', '997333444', '996444555', '995555666', '994444777', '993333888'],
    'Cpf': ['111.222.333-44', '222.333.444-55', '333.444.555-66', '444.555.666-77', '555.666.777-88', '666.777.888-99', '777.888.999-00']
}

# Dados de quartos
quartos = {
    'Nro': [101, 102, 103, 104, 105, 106, 107],
    'Preco': [150.00, 250.00, 200.00, 300.00, 180.00, 220.00, 270.00],
    'Descricao': ['Quarto Simples', 'Quarto Duplo', 'Quarto Triplo', 'Quarto Luxo', 'Quarto Econômico', 'Quarto Executivo', 'Quarto Premium']
}

# Dados de status
status = {
    'Nome': ['Confirmada', 'Cancelada', 'Pendente', 'Em Andamento']
}

# Dados de datas
data = {
    'Data': ['2025-05-12', '2025-05-13', '2025-05-14', '2025-05-12', '2025-05-15', '2025-05-16', '2025-05-17'],
    'Nro_quarto': [101, 102, 103, 104, 105, 106, 107],
    'Status': ['Confirmada', 'Pendente', 'Cancelada', 'Em Andamento', 'Confirmada', 'Pendente', 'Cancelada']
}

# Dados de reservas
reservas = {
    'Nro': [1, 2, 3, 4, 5, 6, 7],
    'Nome_status': ['Confirmada', 'Pendente', 'Cancelada', 'Em Andamento', 'Confirmada', 'Pendente', 'Cancelada'],
    'Data_inicio_data': ['2025-05-12', '2025-05-14', '2025-05-16', '2025-05-12', '2025-05-15', '2025-05-16', '2025-05-17'],
    'Numero_quarto_data_inicio': [101, 102, 103, 104, 105, 106, 107],
    'Data_fim_data': ['2025-05-13', '2025-05-16', '2025-05-17', '2025-05-13', '2025-05-16', '2025-05-17', '2025-05-18'],
    'Nro_quarto_data_fim': [101, 102, 103, 104, 105, 106, 107],
    'Data': ['2025-05-12', '2025-05-14', '2025-05-16', '2025-05-12', '2025-05-15', '2025-05-16', '2025-05-17'],
    'Id_cliente': [1, 2, 3, 4, 5, 6, 7]
}

# Criar DataFrames
df_clientes = pd.DataFrame(clientes)
df_quartos = pd.DataFrame(quartos)
df_status = pd.DataFrame(status)
df_data = pd.DataFrame(data)
df_reservas = pd.DataFrame(reservas)

# Escrever no arquivo Excel
with pd.ExcelWriter('reservas_hotel.xlsx') as writer:
    df_clientes.to_excel(writer, sheet_name='cliente', index=False)
    df_quartos.to_excel(writer, sheet_name='quarto', index=False)
    df_status.to_excel(writer, sheet_name='status', index=False)
    df_data.to_excel(writer, sheet_name='data', index=False)
    df_reservas.to_excel(writer, sheet_name='reserva', index=False)

print("✅ Planilha 'reservas_hotel.xlsx' recriada com sucesso!")