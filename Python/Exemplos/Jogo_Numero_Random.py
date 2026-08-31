from random import randint

numero = randint(1,100)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o numero entre 1 e 100: "))
    print(palpite)
    tentativas += 1
    if numero == palpite:
        print("Parabéns, você acertou!")
        break
    elif numero > palpite:
        print("O numero sorteado é maior do que o seu palpite")
    else:
        print("O numero sorteado é menor do que o seu palpite")

print("Tentativas para vencer:",tentativas)
    
