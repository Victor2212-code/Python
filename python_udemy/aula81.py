# Função lambda em Python
# A função lambda é uma função como qualquer outra em Python. Pórem, são funções anómimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda' },
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [2,3, 5,5, 6, 7, 8, 9,9]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda' },
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
