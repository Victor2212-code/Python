substituicoes = {
    "A": "@", "a": "@",
    "E": "€", "e": "€",
    "I": "!", "i": "!",
    "O": "ø", "o": "ø",
    "U": "µ", "u": "µ",
    "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "&", "7": "*",
    "8": "(", "9": ")", "0": "°"
}

def substituir_caracteres(senha):
    nova_senha = ""
    for caractere in senha:
        if caractere in substituicoes:
            nova_senha += substituicoes[caractere]
        else:
            nova_senha += caractere
    return nova_senha

while True:
    senha = input("Digite sua senha (ou 'sair' para encerrar): ")
    
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    
    if len(senha) < 8:
        print("Senha muito curta. Deve conter pelo menos 8 caracteres.")
    else:
        nova_senha = substituir_caracteres(senha)
        print("Nova senha:", nova_senha)
