def fibonacci(n):
    fibonacci_seq = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

try:
    n = int(input("Digite o valor de 'n' para a sequência de Fibonacci: "))
    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        result = fibonacci(n)
        print(f"A sequência de Fibonacci até o {n}º termo é: {result}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
