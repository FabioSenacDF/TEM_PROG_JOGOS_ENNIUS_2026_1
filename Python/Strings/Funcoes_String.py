# Funções de String

# # Declarações de String
# nome = "Mariana"
# frase = "Olá\nBem-vinda!"
# print(nome)
# print(frase)
# texto_multi_linha = """Nome: Mariana
# Idade: 17
# Estado: DF
# """
# print(texto_multi_linha)

###############################################################

# # Fatiamento de String
# palavra = "Hipopotomonstrosesquipedaliofobia"
# print(palavra)
# print(palavra[8])
# print(palavra[8:16]) # Intervalo, esquerda incluso, direita exclusivo
# fobia_texto = palavra[28:33]
# print(fobia_texto)
# print(palavra[:10]) # Do início até índice(exclusivo)
# print(palavra[21:]) # Do indíce até o fim
# print(palavra[::2]) # Palavra toda pulando de 2 em 2
# print(palavra[::-1])# Palavra toda de trás pra frente

###############################################################

# # Alteração de Caixa
# frase = "Jogos Digitais é área mais legal"
# print(frase)                # Texto original
# print(frase.lower())        # Caixa baixa
# print(frase.upper())        # Caixa alta
# print(frase.capitalize())   # Caixa alta apenas na primeira palavra
# print(frase.title())        # Caixa alta na primeira letra em cada palavra
# print(frase.swapcase())     # Inverte as caixas do texto original

###############################################################

# # Remoção de caracteres e espaços
# frase = " Olá, Bilbo!  "  # Um espaço no início e 2 no fim
# print(frase)
# print(frase.strip())    # Remove espaços em branco no início e no fim
# print(frase.lstrip())   # Remove espaços em branco no início
# print(frase.rstrip())   # Remove espaços em branco do fim

# exemplo = "@EXEMPLO@"
# print(exemplo.strip("@"))   # Remove caractere específico nas pontas
# print(exemplo.lstrip("@"))  # Remove caractere específico no início
# print(exemplo.rstrip("@"))  # Remove caractere específico no fim

###############################################################
# Substituição de Conteúdo (substring)

texto = """

"""
print(texto.replace("antigo","novo"))
