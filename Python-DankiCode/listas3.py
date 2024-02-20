"""
#  index     0        1      2

lista = ["carro", "barco", "avião"]

print(lista)


#  lista.insert(, "bicicleta")
#  lista.append(["Bicicleta", "navio"])
lista.extend(["bicicleta", "navio"])


print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])


"""
"""
#           0       1         2
lista = ["carro", "barco", "avião"]
print(lista)
"""

# lista.pop()
#  lista.remove("barco")

# del lista[0]
# del lista
"""

carrinho_de_comprar = ["pão", "carne", "alface"]
carrinho_de_comprar.sort()

"""
"""
carrinho_de_comprar = ["pão", "carne", "verduras", "alface"]
carrinho_de_comprar.sort()

lista = [1, 50, 23, 67, 100 ]
print(lista)
lista.sort()
# lista.sort(reverse= True)
# carrinho_de_comprar.clear()
lista.reverse()
print(lista)
print(carrinho_de_comprar)

"""


"""for x in range(len(carrinho_de_comprar)):
    print(x, lista[x])
"""
"""
lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
print(lista)

lista.sort(key = str.lower)
print(lista)
"""

'''lista = ["a", "b", "c"]
lista2 = [1, 4, 6]

"""lista = lista + lista2
print(lista)"""

"""lista.extend(lista2)
print(lista)"""

for x in lista2:
    lista.append(x)

print(lista)

'''

lista = ['a', 'b', 'c']
print(lista)


lista2 = lista.copy()
print(lista2)

lista2.append("d")
lista.append("e")

print(lista)
print(lista2)
