# Variável comum, armazena apenas um valor
# pokemon = "Abra"
# Tupla = lista com vários valores fixos
pokemons = ("Charizard","Eevee","Pikachu", "Bastiodon", "Moltres", "Snorlax","Charizard")

print(pokemons[2])                  # Acessar pelo índice
print(pokemons[-1])                 # Acessar pelo índice de tras para frente
# Não é possível alterar valores de uma tupla
#pokemons[0] = "Blastoise"
print(len(pokemons))                # Tamanho da tupla
print(pokemons.count("Charizard"))  # Quantidade de ocorrencias daquele caso
print(pokemons.index("Bastiodon"))  # Índice do primeiro elemento 

for p in pokemons:
    print(p)

##################################################################################]
idades  = (12,45,36,67,98,27,42,54)
print(idades[3])
print(idades[-2])
print(len(idades))                
print(idades.count(67)) 
print(idades.index(42))
print(sum(idades))              # Soma de todos os valores numericos
print(sum(idades)/len(idades))  # Aplicação da fórmula da média

from statistics import mean
print(mean(idades))
