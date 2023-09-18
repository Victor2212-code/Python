def adicionar_conta(contas, total):
    print("Selecione o tipo de conta:")
    print("[1] Água")
    print("[2] Aluguel")
    print("[3] Luz")
    print("[4] Parcela do automóvel")
    print("[5] Supermercado")
    print("[6] Internet")
    print("[7] Gás")
    print("[8] Outro")

    conta = int(input("Digite o número correspondente ao tipo de conta: "))

    tipos_contas = {
        1: 'Água',
        2: 'Aluguel',
        3: 'Luz',
        4: 'Parcela do automóvel',
        5: 'Supermercado',
        6: 'Internet',
        7: 'Gás',
        8: 'Outro'
    }

    if conta not in tipos_contas:
        print("ERRO: Opção inválida.")
        return contas, total

    nome_conta = tipos_contas[conta]
    valor_conta = int(input(f"Adicione o valor da conta de {nome_conta}: "))

    contas.append(nome_conta)
    total += valor_conta

    return contas, total


total = 0
contas = []

while True:
    contas, total = adicionar_conta(contas, total)

    continuar = input("Deseja adicionar mais contas? (S/N): ").lower()
    if continuar != 's':
        break

print(f"Total gasto: R${total}")
print(f"Contas adicionadas: {', '.join(contas)}")
