"""

do while

Código para adivinhar um número

"""
from random import randint

palpite = 0
numero = randint(1, 10)

while True:  # Nós executamos sem verificar
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero:  # Estamos verificando nosso código
        print("Parabens voce acertou")
        break
    else:
        print("Voce errou")

else:
    print("Erro na aplicação")
    print(bool(palpite))
