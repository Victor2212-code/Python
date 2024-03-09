# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática 
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, pórem aceitam apenas 
# Tipos imutáveis como valor interno.

# Criando um set 
# set(iterável) ou {1,2,3}
# s1 = set('Luiz')
# s1 = set() # vazio
# s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
# l1 = [1, 2,3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# # s1 = {1, 2,3, 3, 3, 3, 3, 1}
# s1 = {1, 2, 3}
# # print(3 in s1)

# # for numero in s1:
# #     print(numero)



# # Métodos úteis:
# # add, update, clear, discard 
# s1 = set()
# s1.add('Luiz')
# s1.add(2)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# s1.discard('Luiz')
# # print(s1)

# # Operadores úteis:
# # união | união (union) - Une
# # intersecção & (intersection) - Itens presentes em ambos
# # diferença - Intens presentes apenas no set da esquerda
# # diferença simétrica ^ - Itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2,3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
# s3 = s2 ^ s1

# print(s3)

# Exemplo de uso dos sets
letras  = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    
    if 'l' in letras:
        print('PARABÉNS')
        break

    
    print(letras)
    