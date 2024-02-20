""""#  Paradigma imperativo
#  imperare
#  variáveis, atribuições e principalmente sequêncial

#  C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2.

# bloco externo
nome = "Gabriel"  # variavel global


def minha_funcao():
    bloco interno *bloco interno de uma função é conhecido como corpo
   da função
    nome = "Ana"  # variável local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno do condição if")
    for x in tupla:
        print(x)


minha_funcao()
"""
"""lista = [1, 2, 3, 4, 5]

print(lista)

retorno = lista.pop()
var1 = print("Olá mundo")
print(lista)
print("O retorno da função pop: ", retorno)
print("Retorno da função print: ", var1)"""


"""def ola_mundo():
    print("Olá Mundo")


print(ola_mundo())
"""


"""def par_impar(num):
    if (num % 2) == 0:
        print("Número par")
    else:
        print("Número ímpar")


par_impar(5)
"""


def par_impar():
    numero = 23
    if (numero % 2) == 0:
        return "número par"
    return "número ímpar"


print("ola mundo")
print(par_impar())
print("ola mundo novamente")
