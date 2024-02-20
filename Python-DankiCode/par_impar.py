"""
Como descobrir se um número é impar ou par
"""
print(40 * "-")
numero = int(input("Insira um numero para saber se o mesmo eh par: "))
if (numero % 2) == 0:
    print(f"{numero} eh um numero par")
else:
    print(f"{numero} eh um numero impar")
print(40 * "-")
