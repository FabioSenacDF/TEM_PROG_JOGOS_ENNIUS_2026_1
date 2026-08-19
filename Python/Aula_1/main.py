#print("Hello World")
'''
nome = "Bruno"
print(nome)
nome_pessoa = "Nayara"
print(nome)
'''

#a = 5
#b = 3

# OPERADORES ARITMETICOS
#c = a + b   # ADIÇÃO
#c = a - b   # SUBTRAÇÃO
#c# = a * b   # MULTIPLICAÇÃO
#c = a / b   # DIVISÃO
#c = a % b   # DIVISÃO QUE RETORNA O RESTO
#c = a ** b  # POTÊNCIA
#print(c)

# OPERADORES RELACIONAIS
a = 4
b = 2

#resultado = a > b      # MAIOR
#resultado = a >= b     # MAIOR OU IGUAL
#resultado = a < b      # MENOR
#resultado = a <= b      # MENOR OU IGUAL
#resultado = a == b     # IGUAL
#resultado = a != b     # DIFERENTE
#print(resultado)

# OPERADORES LÓGICOS
# c = 2
# d = 7

# resultado_log = c < d and c > 0 # 2 lados devem ser True para resultado True
# resultado_log = c > d or c > 5  # apenas um lado deve ser True para resultado True
# print(resultado_log)
# afirmacao = 1 > 3
# negacao = not afirmacao
# print(afirmacao)
# print(negacao)

# peso = float(input("Digite o peso: "))

# if peso >= 120:
#     print("Peso acima do permitido!")
# elif peso < 120 and peso >=20:
#     print("Tobogã liberado!")
# elif peso < 20 and peso >=0:
#     print("Peso abaixo do permitido!")
# else:
#     print("Peso inválido!")

# DESAFIO: Usuario digita a idade e programa diz se é
# maior ou menor de idade

idade = int(input("Digite a sua idade: "))

if idade >= 60:
    print("Idoso")
elif idade < 60 and idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 12:
    print("Adolescente")
elif idade < 12 and idade >= 4:
    print("Criança")
elif idade < 4 and idade >= 0:
    print("Bebe")
else:
    print("Idade invalida")
