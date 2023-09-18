senha_correta = 221204
tentativas = 3

while True:
    senha = input("Digite a senha: ")

    try:
        senha = int(senha)
    except ValueError:
        print("Por favor, digite um número inteiro para a senha.")
        continue

    if senha == senha_correta:
        print("Seja Bem Vindo!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta.")

        if tentativas == 0:
            print("Número máximo de tentativas excedido.")
            break

        opcao = input("Deseja tentar novamente? (S/N): ")
        if opcao.upper() != 'S':
            break
