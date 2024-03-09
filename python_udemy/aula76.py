# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser considerados como o "índice" que vimos na lista e podem ser de tipos imutáveis como : str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, inclindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#          'nome': 'Victor Hugo',
#           'sobrenome': 'Assumpção', 
#           'idade' : 19,
#            'altura': 1.8,
#            'endereços': [{'rua': 'tal tal', 'numero': 123}, {'outra rua': 'tal tal', 'numero': 321}]
# 
# pessoa = {
#     'nome': 'Victor Hugo',
#           'sobrenome': 'Assumpção', 
#           'idade' : 19,
#            'altura': 1.8,
#            'enderecos': [{'rua': 'tal tal', 'numero': 123}, {'outra rua': 'tal tal', 'numero': 321}]
# }
# print(pessoa['sobrenome'], type(pessoa))

# for chave in pessoa:
#     print(chave, pessoa[chave])

# Manipulando chaves e valores em dicionários
# pessoa = {
#     'nome': 'Victor Hugo',
#           'sobrenome': 'Assumpção', 
#           'idade' : 19,
#            'altura': 1.8,
#            'enderecos': [{'rua': 'tal tal', 'numero': 123}, {'outra rua': 'tal tal', 'numero': 321}]
# }
# print(pessoa['sobrenome'], type(pessoa))

# for chave in pessoa:
#     print(chave, pessoa[chave])

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'


# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is not None:
#     print('Não Existe')
# else:
#     print(pessoa['nome'])


# Métodos úteis dos dicionários em Python
# len - quantas chaves 
# keys - iterável com as chaves 
# values - iterável com os valores 
# items - iterável com chaves e valores 
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro 

# import copy

# d1 = {
#     'c1': 1, 
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 999999
# print(d1)
# print(d2)

p1 = {
    'nome': 'Luiz', 
    'sobrenome': 'Miranda', 
}
# print(p1['nome'])
# print(p1.get('nome', 'Não Existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'Osavaldo'], ['idade', 20]]
p1.update(lista) 
print(p1)