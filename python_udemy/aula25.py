"""
Interpolação básica de strings 
s- strings 
d e i - int 
f - float 
x e X - Hexadecimal(ABCDEF012346789)
"""


nome = 'Luiz' 
preco = 100.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é  %04X' % (10000, 10000))