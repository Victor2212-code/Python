""""class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado

    def retorna_area(self):
        print(self.__area)


quadrado = Quadrado(3)
quadrado.retorna_area()
quadrado.area = 7
quadrado.retorna_area()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13
quadrado.retorna_area()

#   Name Mangling __Classe__atributo"""

"""
class Aluno:

    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.matricula = matricula
        self.notas = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property  # decorador property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


aluno = Aluno('Victor', 15, 1233456)

print(aluno.nome)
aluno.nome = 'Marcos'
print(aluno.nome)

print(aluno.idade)
aluno.idade = 17
print(aluno.idade)
"""


# Classe Abstrata


# 4 níveis de herança

# Classe Abstrata




from abc import ABC, abstractmethod
class Pessoa(ABC):
    # superclasse - classe mãe, classe pai

    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print('Executando o construtor da Classe Pessoa')

    def impirimir_nome(self):
        return self.nome

    @abstractmethod
    def trabalhar(self):
        print("Implemente a funcionalidade deste método")


class Administrador(Pessoa):
    # subclasse - classe filha, classe filho
    def trabalhar(self):
        return super().trabalhar()


class Professor(Pessoa):
    # subclasse - classe filha, classe filho
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Ensinando....')

# Classe Concreta


class Aluno():
    # subclasse - classe filha, classe filho
    def __init__(self, nome):
        super.__init__(nome)
        self.matricula = matricula
        self.notas = []
        print("Classe Aluno")

    def estudar(self):
        return 'Estudando....'


professor1 = Professor("Marcos")
administrador1 = Administrador()
administrador1.trabalhar()
professor1.trabalhar()

# Herança trata da relação entre classes
