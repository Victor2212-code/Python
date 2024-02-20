"""
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
 de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado

03 - Se o produto que você quer avaliar custa (??) reais
qual será o valor do mesmo com desconto de (??)%.

04 - área de um círculo
05 - conversão de reais para dolar
06 - conversão de dolar para reais

"""
'''
Exercício 1
print("Calcule a área de um retangulo")

base = float(input("Qual o tamanho da base do seu retangulo?"))
altura = float(input("Qual o tamanho da altura do seu retangulo? "))
area = base * altura

print(f"A área do retangulo mede: {area} unidade de medida")
'''

"""
Execício 2

base = float(input("Digite a base do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))
area = base * altura

print(f"A area do quadrado é: {area}")

"""
'''
Exercicio 3

produto_preco = float(input("Digite o valor do produto: "))
produto_desconto = produto_preco - (produto_preco * 0.35)
print(f"O valor final com desconto é: {produto_desconto}")

'''
"""
Execício 4
pi = 3.1415

raio = float(input("Digite o raio da circunferência: "))
area_circulo = pi * raio ** 2

print(f"A área do círculo é: {area_circulo:,.2f}")

"""

"""

Exercício 5

real = float(input("Digite o valor que deseja converter: R$ "))
dolar = real / 4.91

print(f"O total em dólares é: {dolar:,.2f}")

"""

"""

Execício 6

dolar = float(input("Digite o valor que deseja converter: U$ "))
real = dolar / 0.20

print(f"A quantidade de dolares em reais é: {real:,.2f}")

"""
