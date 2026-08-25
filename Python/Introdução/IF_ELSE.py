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
