digito = input("Digite uma numero e descubra a quantidade de digitos: ")

contagem = 0

for letra in digito:
    if letra.isdigit():
        contagem += 1

print("A quantidade de dígitos é: ", contagem)
