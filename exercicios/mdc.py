def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a


primeiro_numero = int(input("Digite o primeiro número inteiro: "))
segundo_numero = int(input("Digite o segundo número inteiro: "))

mdc = calcular_mdc(primeiro_numero, segundo_numero)

print(f"O MDC de {primeiro_numero} e {segundo_numero} é {mdc}")
