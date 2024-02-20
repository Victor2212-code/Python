

lista1 = [2.0, 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

#  0         1           2         3        4           5
lista3 = ["gato", "cachorro", "peixe", "cavalo", "Tubarao", "girafa"]

print(len(lista3))

# tamanho da lista - função len

print(len(lista1))
print(len(lista2))

# funções que só  podem ser utilizadas com tipos de dados númericos

print(sum(lista1))  # Somatorio dos elementos da nossa lista

x = 2.0 + 3.5 + 4.7
print(x)

print(max(lista2))  # Retorna o elemento do valor máximo da lista
print(max(lista1))

print(min(lista2))  # Retorna o elemento de valor minimo da lista
print(min(lista1))

nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list('Curso de Python')
print(lista8)

elemento = 8
if elemento in lista7:
    print("Este elemento está dentro da lista")

"""lista3[1] = 'cavalo'
print(lista3)

lista3[1:4] = ["águia", "morcego", "elefante"]
print(lista3)


lista3[1:2] = ["águia", "elefante"]
print(lista3)

print(lista3[1])
print(lista3[2])
print(lista3[3])"""

lista3[1:5] = ["tubarao"]
print(lista3)
print(len(lista3))
