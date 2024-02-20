# Desempacotamento em chamadas]
# de métodos e funções 

# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'

# # p, b, *_, ap, u = lista
# # print(p, u, ap)
# print(*tupla)
# print(*lista)
# print(*string)

salas = [
    # 0         1 
    ['Maria', 'Helena'], # 0 
    # 0 
    ['Elaine'], # 1 
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'], #2
]

print(*salas, sep='\n')