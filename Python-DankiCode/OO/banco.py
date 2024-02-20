"""
Aclopamento

"""
"""
Visibilidade - Modificador de acessso

privada(private) - restritiva --> Define que os atributos só podem ser manipulados dentro da classe que foram definidos.
protegida(potected) - intermediária --> Define que os atributos e métodos só podem ser manipulados dentro das classes que elas foram definadas, e nas classes que herdam da classe onde foram definidos.
publica(public) - menos restritiva --> define que os atributos e medos podem ou são assesiveis em qualquer parte do codigo

"""


class Conta:

    # Atributo de Classe
    taxa = 0.50

    @staticmethod
    def retornarCodigoBanco():
        return "345"

    # Atributos de instância
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero  # visibilidade protegida (protected)
        self.titular = titular  # visisbilidade publica (public)
        self.__saldo = saldo  # visibilidade privada (private)
        self.__historico = [saldo]

    def Saldo(self):
        print(f"Saldo: R$ {self.__saldo} ")

    def Transacao(self, saldo):
        self.__historico.append(saldo)

    def Extrato(self):
        print('----Extrato------')
        print(f'Conta: {self.titular}')
        for saldo in self.__historico:
            print(f"Saldo: R$ {saldo} ")

    def Depositar(self, valor):
        self.__saldo += valor
        self.Transacao(self.__saldo)

    def Sacar(self, valor):
        self.__saldo -= valor
        self.Transacao(self.__saldo)

    def Transferir(self, valor, destino):
        self.Sacar(valor)
        destino.Depositar(valor)


"""
# Instância da Classe Conta
conta1 = Conta(123456, "João Carlos")
conta2 = Conta(4563145, "Maria Antonieta", 5600)

print(conta1.__dict__)
print(conta2.__dict__)

print(conta2.Extrato())

# Atributo Dinâmico - Criado em tempo de execução
conta2.signo = 'Peixes'

print(conta1.__dict__)
print(conta2.__dict__)

del conta2.signo
print(conta2.__dict__)

# Método da Classe
Conta.retornarCodigoBanco()  # Convenção
conta1.retornarCodigoBanco()

# Método Estático
print(Conta.retornarCodigoBanco())  # Convenção
print(conta1.retornarCodigoBanco())
"""

conta1 = Conta(123, 'Mona Lisa', 2300)
conta2 = Conta(345, 'Albert')

conta1.Transferir(300, conta2)
print(conta2.Saldo())
print(conta1.Saldo())
conta1.Transferir(662, conta2)
conta1.Extrato()