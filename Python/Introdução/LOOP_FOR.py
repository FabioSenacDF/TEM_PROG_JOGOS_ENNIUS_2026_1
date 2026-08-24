import time

# for i in range(100,-2,-2):
#     print(i)
#     time.sleep(1)
    
somatorio = 0
media = 0
quantidade = int(input("Digite quantos numeros quer somar: "))
# receber a quantidade de numeros digitados antes do loop

for i in range(quantidade):
    num = float(input("Digite o número "+str(i+1)+" : "))
    #somatorio = somatorio + num
    somatorio += num

print("Somatório:",somatorio)
media = somatorio/quantidade
print("Média:",media)
