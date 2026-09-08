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
# # Remover elementos
# carrinho_compras = {
#     "mouse" : 79.99,
#     "teclado_gamer" : 249.99,
#     "monitor" : 1499.49,
#     "placa_RTX" : 29999.00
# }

# # Anular o valor 
# carrinho_compras["teclado_gamer"] = None

# # Remove e retorna valor
# preco_mouse = carrinho_compras.pop("mouse")
# print("Preço do mouse:",preco_mouse)

# # Remove par sem retornar
# del carrinho_compras["monitor"]

# # Remove ultimo par (chave:valor) como tupla
# ultimo = carrinho_compras.popitem()
# print(ultimo)

# # Limpar Dicionário
# carrinho_compras.clear()

# print(carrinho_compras)

##############################################
# Iteração (laços de repetição)

#faturamento = {"jan":1000, "fev":1500, "mar":1800}

#for mes in faturamento.keys():  # Iteração nas chaves
    #print(mes)

#for val in faturamento.values(): # Iteração nos valores
    #print(val)

#for mes,val in faturamento.items():# Iteração no par
    #print(f"No mês {mes} o faturamento foi R${val}")

##############################################
# Dicionário Aninhado, similar a JSON

banco_de_dados = {
    "cliente_1":{
        "nome":"Ana",
        "compras":["Livro","Caneta"]
    },
    "cliente_2":{
        "nome":"Bruno",
        "compras":["Caderno","Tesoura"]
    },
    "cliente_3":{
        "nome":"Caio",
        "compras":["Borracha","Livro"]
    }
}
nome_cliente_1 = banco_de_dados["cliente_1"]["nome"]
print(nome_cliente_1)

primeira_compra_bruno = banco_de_dados["cliente_2"]["compras"][0]
print(primeira_compra_bruno)

lista_compras_caio = banco_de_dados["cliente_3"]["compras"]
print(lista_compras_caio)
