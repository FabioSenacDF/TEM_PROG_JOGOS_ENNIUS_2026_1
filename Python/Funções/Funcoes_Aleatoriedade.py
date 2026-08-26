# Funções
'''
# Função sem argumento
def saudacao():
    print("Olá")
    print("Tudo bem?")

saudacao()

# Função com argumento
def boasvindas(nome,sobrenome):
    print("Bem-vindo(a):",nome,sobrenome)

boasvindas("Pedro", "Machado")
boasvindas(sobrenome="Rossi",nome="Marcelo")

# Função com argumento padrão
def msg(nome, mensagem=", tudo bem?"):
    print(nome+mensagem)

msg("João")
msg("João",", como está?")
msg("João", mensagem = ", blz?")

# Função com retorno
def pi():
    return 3.141592653589793

print(pi())

# Criar função somar que recebe a e b 
# e retona a soma entre os dois
def somar(a,b):
    return a+b

resultado_soma = somar(6,7)
print(resultado_soma)
'''
from random import randint

def jogar_dados(lados):
    resultado = randint(1,lados)
    return resultado

while True:
    entrada_input = input("Digite a quantidade de lados do dado")
    entrada_int = int(entrada_input)

    if entrada_int == 0:
        break
    else:
        result = jogar_dados(entrada_int)
        print(result)

print("FIM")
