inicio_sequencia = int(input("Digite o número inicial da sequência: "))
termino_da_sequencia = int(input("Digite o número de término da sequência: "))

quantidade_primos = 0

for numero in range(inicio_sequencia, termino_da_sequencia + 1):
    if numero > 1:
        e_primo = True
        for i in range(2, numero):
            if (numero % i) == 0:
                e_primo = False
                break
        if e_primo:
            quantidade_primos += 1

print("Quantidade de números primos no intervalo:", quantidade_primos)
