palavra = input("Digite uma palavra: ")

vogal = ["a", "A", "e", "E", "e", "i", "I", "o", "O", "u", "U"]


contagem_vogais = 0

for letra in palavra:
    if letra in vogal:
        contagem_vogais += 1

print(f"A palavra digitada tem {contagem_vogais}")
