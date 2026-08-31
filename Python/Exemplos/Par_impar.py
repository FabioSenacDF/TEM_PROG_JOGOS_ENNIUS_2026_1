# Verificar se numero é par ou ímpar
numero = int(input("Digite um numero: "))
# Verificar o tipo de variável
print(type(numero))

resto = numero % 2

if resto == 0:
    print("Par")
else:
    print("Ímpar")
