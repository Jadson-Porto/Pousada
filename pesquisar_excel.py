import pandas as pd

# Carregar o arquivo Excel
arquivo = "reservas_hotel.xlsx"

# Ler a planilha específica (substitua 'cliente' pelo nome da planilha que deseja pesquisar)
df = pd.read_excel(arquivo, sheet_name="cliente")

# Exibir os dados carregados
print("Dados carregados:")
print(df)

# Pesquisar por um cliente específico (exemplo: nome do cliente)
nome_cliente = "João Silva"
resultado = df[df['nome'] == nome_cliente]

# Exibir o resultado da pesquisa
if not resultado.empty:
    print(f"\nResultado da pesquisa para o cliente '{nome_cliente}':")
    print(resultado)
else:
    print(f"\nCliente '{nome_cliente}' não encontrado.")