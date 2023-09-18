from random import randint as rand

aleatorio = rand(1, 8)

num_usuario = int(input("Advinhe o número oculto: "))


if num_usuario == aleatorio:
    print("Parabéns!!!!, Você acertou o número")
else:
    print(f"O {num_usuario} não é o número oculto")
