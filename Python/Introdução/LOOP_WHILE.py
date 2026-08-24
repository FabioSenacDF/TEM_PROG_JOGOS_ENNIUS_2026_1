# somatorio = 0

# while somatorio <= 100:
#     num = float(input("Digite um numero: "))
#     somatorio += num

# print(somatorio)

somatorio = 0
contador = 0

while True:
    num = float(input("Digite um numero (0 para parar): "))
    if num == 0:
        break
    somatorio += num
    contador += 1
    
print("Somatório:",somatorio)    
print("Contador:",contador)    
print("Média:",somatorio/contador)    
