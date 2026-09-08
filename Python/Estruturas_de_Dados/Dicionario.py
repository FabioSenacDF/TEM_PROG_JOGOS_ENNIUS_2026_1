# Dicionário {}

# Dicionário Vazio
# dic_vazio = {}
# dic_vazio_2 = dict()

# ##############################################
# # Par chave(string):valor(qualquer um)

# aluno = {
#     "nome": "Henrique",
#     "idade":26,
#     "curso":"Programação de Jogos Digitais",
#     "trancado": True
# }
# #print(aluno)

# print(aluno["nome"])
# print(aluno["idade"])
# print(aluno["curso"])
# print(aluno["trancado"])
# #print(aluno["UC"])    # Chave inexistente (erro)
# idade = aluno.get("idade")
# print(idade)
# uc = aluno.get("uc")   # Chave inexistente (não gera erro)
# print(uc)

##############################################
# # Adicionar e modificar valores

# perfil_game = {"usuario": "Godot Master","cash": 500}
# perfil_game["patente"] = "Prata"
# perfil_game["cash"] = 600
# perfil_game.update(
#     {
#         "cash":1000,
#         "ultimoLogin":"08-09-26 14:52:41",
#         "patente": "Ouro"
#     }
# )

# print(perfil_game)

##############################################
# Remover elementos
carrinho_compras = {
    "mouse" : 79.99,
    "teclado_gamer" : 249.99,
    "monitor" : 1499.49,
    "placa_RTX" : 29999.00
}

# Anular o valor 
carrinho_compras["teclado_gamer"] = None

# Remove e retorna valor
preco_mouse = carrinho_compras.pop("mouse")
print("Preço do mouse:",preco_mouse)

# Remove par sem retornar
del carrinho_compras["monitor"]

# Remove ultimo par (chave:valor) como tupla
ultimo = carrinho_compras.popitem()
print(ultimo)

# Limpar Dicionário
carrinho_compras.clear()

print(carrinho_compras)
##############################################

