"""# Parâmetros de um função

def nome_da_funcao(nome):  # parametro e o nome dado aos valores
    # utilizados na definição de uma função

    #  corpo da função
    print(f"Olá {nome}")


nome = input("Qual é seu nome: ")
# argumento é o nome dado aos valores utilizados na chamada de um função
nome_da_funcao(nome)
"""


"""def imprime_nome(nome, sobrenome):
    print(f"olá, {nome} {sobrenome}")


nome = "Maria"
sobrenome = "Aparecida"


imprime_nome(nome, sobrenome)
"""

#  Argumentos nomeados

"""
def imprimir_nome(nome, sobrenome, idade):
    print("Nome:  ", nome)
    print("Sobrenome:  ", sobrenome)
    print("Idade:  ", idade)


sobre_nome = "clara"
idade = 35
imprimir_nome(nome="Victor", idade=idade,  sobrenome=sobre_nome)
"""

# Parâmetro padrão - Define argumentos não obrigatórios

""""
def imprimir_imovel(NomeImovel=None, vagasGaragem=None, n_quartos=None):
    print("-------------")
    print("Título: ", NomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem:  ", vagasGaragem)


print()
# Exemplo de n° de argumentod <=  n° dos parâmetros
imprimir_imovel("Mansão", 25, 3)
imprimir_imovel("Apartamento", 4, 1)


#  Exemplos de números de argumentos > que os números dos parãmetros
imprimir_imovel("Loja Comercial", 2, 5, "desconto")
"""

# Argumento Arbitrário *args - utilizado quando não se sabe quantos argumentos
#  essa função vai receber, o que ele faz é guarda os valores dentro
#  de uma tupla.

#  Essa função recebe argumentos que serão atribuidos a uma tupla.

"""
def imprimir_imovel(NomeImovel, vagasGaragem, n_quartos=None, *telefones):
    print("-------------")
    print("Título: ", NomeImovel)
    print("Quartos: ", n_quartos)
    print("Telefones: ", telefones)
    if vagasGaragem != None:
        print("Vagas na garagem:  ", vagasGaragem)


imprimir_imovel("Loja Comercial", 2, 5, "61 5555-555555", "21 5555-55555")


def imprimir_nomes(nomes):
    print(nomes)
    print(type(nomes))


lista = ["ana", "beatriz", "pedro", "joão"]
imprimir_nomes(lista)
"""

#  Argumento Arbitrário *Kwags - KEYWORD ARGUMENTS
# Essa função recebe argumentos que serão atribuidos em um dicionário.


""" def imprimir_nomes(nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")

dicio = {'nome': "ana", 'sobrenome': 'julia'}
imprimir_nomes(dicio)"""
