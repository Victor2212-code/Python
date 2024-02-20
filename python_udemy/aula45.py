"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez 
next -> me entregue seu iterador
iter -> me entregue seu iterador
"""
# for letra in texto 
texto = 'Luiz' # iterável 

# iterador = iter(texto) # iterator

# while True:
#     try:
#         print(next(iterador))
        
#     except StopIteration:
#         break

for letra in texto:
    print(letra)