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

# texto = """
# antigo
# """
# print(texto.replace("antigo","novo"))

###############################################################
# Verificação de conteúdo

#frase = "A IA irá dominar o mundo"
#print("IA" in frase)         # Verifica se a string contém uma substring
#print("AI" in frase)
#print(frase.startswith("A"))  # Verifica se a string inicia com uma substring
#print(frase.startswith("a"))
#print(frase.endswith("mundo"))# Verifica se a string termina com uma substring
#print(frase.endswith("mund"))

#print(len(frase))       # Verificar tamanho(conta espaços)
#print(frase.count("o")) # Verifica quantidade de caracteres correspondentes
#print(frase.count("H"))

###############################################################
# Divisão de Strings

# frase = "Aprender Python é legal"
# # Separa pelo caractere indicado e cria lista (espaço se não for indicado)
# lista_palavras = frase.split("")
# print(lista_palavras)
# print(lista_palavras[1])

# for p in lista_palavras:
#     print(p)

###############################################################
# Junção de Strings
# lista_palavras = ["Minecraft","foi","feito","em","Java"]
# # Junta elementos de uma lista usando caractere como separador
# frase_completa = " ".join(lista_palavras)
# print(frase_completa)

###############################################################
# Encontrar posição de palavra ou caractere

# frase = "Um mago nunca se atrasa"
# print(frase.find("mago"))   # Encontra índice da primeira ocorrência
# print(frase.find("m"))
# print(frase.find("bruxo"))  # Retorna -1
# print(frase.index("mago"))  # Encontra índice da primeira ocorrência
# print(frase.index("bruxo")) # Gera erro

###############################################################

