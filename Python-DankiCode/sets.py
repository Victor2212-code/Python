"""
Lista: Coleção ordenada, mutável e que permite valores duplicado
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionario: Coleção não ordenada, mútavel e que não permite valores duplicados
Sets: Coleção não ordenada, imutável e que não permite valores duplicados
"""

#  Os sets também são conhecidos como conjuntos

"""conjunto = {"item1", 3, True, 4.7, "sao paulo"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))"""

"""tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)

print(type(conjunto))"""

"""conjunto = {3, 7, 9, 5}
print(conjunto)"""

#  Acessando os itens do meu set

"""conj = {"item1", "item2", "item3", "item4"}

for x in conj:
    print(x)
"""

"""conjunto = {"item1", 6, 8, 9, 1}
print("item2" in conjunto)"""

#  adicionou elementos
"""set1 = {"item1", "item2", "item3"}

print(set1)
set1.add("item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1)

"""

"""set1 = {4, 5, 7, 8, 9, 1}
set1.update([1, 4, 7, 8, 9, 3])
print(set1)
"""

"""
#  Removendo elemntos
set1 = {4, 5, 7, 8, 9, 1, "item1", "item2"}
print(set1)

set1.pop()
print(set1)

set1.remove("item1")
print(set1)

set1.discard(9)
print(set1)

set1.clear()
print(set1)"""

# utilizando funções principais dos sets
"""conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

conjunto1.update(conjunto2)
print(conjunto1)"""

#  utilizando as funções principais dos sets

"""conjunto1 = {1, 5, 6, 2}
conjunto2 = {3, 6, 2}

conjunto1.update(conjunto2)

print(conjunto1)"""


"""conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto1.intersection_update(conjunto2)
print(conjunto1)"""

conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}


conjunto1.symmetric_difference_update(conjunto2)
conjunto1 = {1, 5, 6}
print(conjunto1)

#  Diagrma de Venn
