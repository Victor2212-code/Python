import random
from faker import Faker

fake = Faker()

codigo_pessoa = {}
max_pessoas = 100

# Gerar nomes aleatórios e atribuir códigos
for codigo in range(1, max_pessoas + 1):
    nome = fake.first_name()
    codigo_pessoa[codigo] = nome

while True:
    try:
        escolha_usuario = int(
            input(f"Digite o código da pessoa que você deseja encontrar (1-{max_pessoas}) ou 0 para sair: "))

        if escolha_usuario == 0:
            print("Saindo do programa.")
            break

        if escolha_usuario in codigo_pessoa:
            nome_pessoa = codigo_pessoa[escolha_usuario]
            print(f"A pessoa que você procura é {nome_pessoa}")
        else:
            print("Pessoa não encontrada. Verifique o código inserido.")
    except ValueError:
        print("[ERRO] Digite um número válido.")
