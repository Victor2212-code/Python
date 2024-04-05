import copy

from dados import produtos

# copy, sorted, produtos.sort
# Exercícios 
# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene em produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy ( cópia profunda)
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), 
                                     key=lambda p: p['nome'],
                                     reverse=True)

# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# Ordene os produtos por preço crecente (do menor pra maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), 
                                     key=lambda p: p['preco'],
                                     )

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')