def numeros_perfeitos(inicio, fim):
    num_perfeitos = []
    for numero in range(inicio, fim + 1):
        soma_divisores = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                soma_divisores += divisor
        if soma_divisores == numero:
            num_perfeitos.append(numero)

        return num_perfeitos


inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))


numeros_perfeitos_no_intervalo = numeros_perfeitos(inicio, fim)


if numeros_perfeitos_no_intervalo:
    print("Números perfeitos no intervalo:", numeros_perfeitos_no_intervalo)
else:
    print("Nenhum número perfeito encontrado no intervalo.")
