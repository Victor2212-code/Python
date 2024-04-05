# Combination, Permutation e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação -Ordem importa 
# Produto - Ordem importa e repete valores únicos.
from itertools import combinations, product, permutations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pesssoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'], 
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester', ],
]
# print_iter(combinations(pesssoas, 2))
# print_iter(permutations(pesssoas, 2))
print_iter(product(*camisetas))