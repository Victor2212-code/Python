# Paradigma Imperativo

"""
Paradigma Imperativo - Fortran - Sequência, Decisão e a Iteração
Paradigma Estruturado- C - structs
Paradigma Procedural -  Python
"""


def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente

# Reuso e Coesão

# Paradigma Orientado à Objetos

# CamelCase


"""
Classe - Conjunto de objetos com as mesmas características 
Objeto - Representação do mundo real como um tipo de dado de uma classe
Construtor - E a função criada implicitamente  com o mesmo nome da classe
Atributo - São as variaveis de uma classe
"""


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print("Acessei o Construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email


# Reuso e a Coesão
# Aclopamento, Herança, polimorfismo, GAP semântico
"""
    Simulação de Eventos Discretos -> Paradigma Orientado à Objetos
    Relação -> Destrancando funções e variáveis 

-------------------------------------------------------

Conceitos Estruturais

.Classe

Classe é uma estrutura que abstrai um conjunto de objetos com caracteristicas similares. Definindo um conjunto o comportamento dos seus objetos atráves das estruturas:

1 - Atributos 
2 - Métodos


A classe define um tipo de dado abstrato

-Objeto

Um objeto é a representação de um comportamento do mundo real, que pode ser física ou conceitual e possui um significado bem definido para um determinado software.
"""

# Abstração
# Reuso e a Coesão
# Aclopamento, herança, polimorfismo, GAP semântico

"""
    Conceirto Fundamentais

    - Abstração

    Processo pelo qual se isolam atributos de um objeto.
considerando os que certos grupos de objetos tenham em comum.

    -Reúso
    Não existe pior prática em programação do que repetir código

"""
