"""
Iterando strings com while
"""

string = 'Antonio'
iteracao = 0
novo_nome = ''
while iteracao < len(string):
    letra = string[iteracao]
    novo_nome += f'*{letra}'
    iteracao += 1
    
novo_nome += '*'
print(novo_nome)