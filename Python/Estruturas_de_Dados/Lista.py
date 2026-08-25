# Estrutura de Dados - Lista []
'''
# Listas vazias
vazia = []
vazio_2 = list()

numeros = [5,3,8,9,6]
nomes = ["Aragorn", "Legolas","Gimli","Frodo"]
mista = ["Kleber", 26, "01234567891", 1.85, 87, True]

letras = list("Paralelepipedo")
print(letras[0])
print(letras[-1])

# Intervalo, numero da esquerda = inclusivo
# numero da direita = exclusivo
print(letras[4:8])
# Nada à esquerda = 0, início
print(letras[:4])
# Nada à direita = fim
print(letras[8:])
# Inversão da lista
print(letras[::-1])
'''

'''
# Modificando elementos
notas = [8.2, 2.3, 5.6, 7.9, 4.8]
notas[1] = 4
notas[3:5] = [8, 5]
print(notas)
'''

'''
# Adicionar elementos
carros = ["Fusca","Santana","Opala"]
print(carros)
# append = adiciona no final da lista
carros.append("Maverick")
print(carros)
# insert = adiciona na posição do índice indicado
carros.insert(2,"Passat")
print(carros)
# extend = adiciona uma nova lista no fim
carros.extend(["Escort","Chevette"])
print(carros)
'''

# Remover elementos
tarefas = [
    "Comprar",
    "Reabastecer",
    "Limpar",
    "Ler",
    "Comprar",
    "Responder"
]
print(tarefas)
# remove = exclui a primeira ocorrência
tarefas.remove("Reabastecer")
print(tarefas)
# pop = remove o ultimo e pega o valor (retorno)
ultima_tarefa = tarefas.pop()
print(ultima_tarefa)
print(tarefas)
# del = deleta no índice indicado
del(tarefas[1])
print(tarefas)

# Remove todas as ocorrências do elemento
t = "Comprar"
while t in tarefas:
    tarefas.remove(t)

print(tarefas)

# clear = limpa a lista, remove todos os elementos
tarefas.clear()
print(tarefas)
