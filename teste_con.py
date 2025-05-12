from db import criar_conexao

conexao = criar_conexao()
if conexao:
    print("🟢 Conectado com sucesso!")
else:
    print("🔴 Falha na conexão.")