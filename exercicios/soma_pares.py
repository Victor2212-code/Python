def soma_pares(num):
    par = []
    for i in range(1, num + 1):
        if i % 2 == 0:
            par.append(i)
    return par

while True:
    num = int(input("Digite um número positivo: "))
    if num <= 0:
        break
    result = soma_pares(num)
    print(f"A soma dos números pares até {num} é: {sum(result)}")

