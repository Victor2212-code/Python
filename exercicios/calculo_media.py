def calcula_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media


print("Faça a média entre números, basta digitá-los (separados por espaço):")
entrada = input("Digite os números: ")
valores = [float(num) for num in entrada.split()]

media = calcula_media(valores)
print("A média dos números é:", media)
