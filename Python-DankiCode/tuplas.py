#    index     0         1        2        3        4

# nas tuplas não temos funções como a de adicionar e remover, por conta dela
"""ser imutavel (dir(tupla)) para saber as funções, servirndo para
outros tipos de coleções.
"""
"""
tupla = ("item1", "item2", "item3", "item1", "item1")
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])

print(tupla.count("item1"))
tupla.append("item4")
print(tupla)

lista = []
lista.append("item1")
print(lista)"""


"""lista = ["item1", "item2"]
print(lista)
lista[0] = "item3"
print(lista)"""

"""
tupla = ("item1", "item2")
print(tupla)

tupla = ("item3", "item4", "verde")
print(tupla)

"""

# o que define uma tupla não e os parênteses mas sim a vírgula.
"""
tupla = ("item1", "item2", "item3", "item4")
lista = list(tupla)
print(tupla)
print(lista)

lista.pop()
print(lista)

tupla = tuple(lista)
print(tupla)
"""
tupla = ("item1",)
tupla2 = ("a", "b")

tupla = "item1", "item2", "item3", "item4", "item5"
print(tupla)

(x, *y, z) = tupla
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

print(x)
