class Conta:
    def __init__(self, nome, cpf, numero_conta, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo

    def extrato(self):
        print('-' * 50)
        print(f"Nome do titular: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print('-' * 50)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError(
                "Valor de saque inválido. O valor deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")

        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        self.extrato()

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError(
                "Valor de depósito inválido. O valor deve ser maior que zero.")

        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        self.extrato()


def main():
    print("Bem-vindo ao sistema bancário!")

    nome = input('Informe seu nome: ')
    cpf = input('Informe seu CPF: ')
    numero_conta = int(input('Informe o número da conta: '))

    conta = Conta(nome, cpf, numero_conta)

    while True:
        print("\nEscolha uma operação:")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Consultar saldo")
        print("4 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            try:
                valor = float(input('Quanto você deseja sacar? R$'))
                conta.sacar(valor)
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == '2':
            try:
                valor = float(input('Quanto você deseja depositar? R$'))
                conta.depositar(valor)
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo do programa. Obrigado por usar nossos serviços!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
