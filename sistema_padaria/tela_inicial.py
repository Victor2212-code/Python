import gerente
import Padeiro
import vendedor

opcao = int(input('Qual seu tipo de usuário [1]Gerente, [2]Padeiro, [3]Vendedor: '))

match opcao:
    case 2:
        nome = input("Nome: ")
        codigo_identificacao = input("Código identificação: ")
        Padeiro.login(nome, codigo_identificacao)