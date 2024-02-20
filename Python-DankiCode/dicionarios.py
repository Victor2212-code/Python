"""
Listas: Coleção ordenada, mutável e que permite valores duplicados.
Tuplas: Coleção ordenad, imutável e que permite valortes duplicados
Dicionarios: Coleções não ordenada, mutável e que não permite
 valores duplicados mais conhecido como mapas 
"""

#           1        2        3
lista = ["item1", "item2", "item3"]
#           1        2        3
tupla = ["item1", "item2", "item3"]

# chave: valor
dicio = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}

print(dicio)


dicionario = {
    "nome": "Victor",
    "idade": 18,
    "cidade": "Ourinhos",
    "Nacionalidade": "Brasileiro",
    "idade": 35
}

print(dicionario)

print(dicionario["idade"])  # retorna o valor da chave idade

print(dicionario.get("idade"))

print(dicionario.keys())  # retorna todas as chaves

print(len(dicionario))  # retorna o tamanho do dicionario chamado dicionario

print(dicionario.values())  # retorna os valores do dicionario

if "idade56" in dicionario:
    print("A chave idade existe")


# retorna todas as chaves e valores como se fossem listas com tuplas dentro.
print(dicionario.items())
