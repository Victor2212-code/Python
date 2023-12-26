import re


def validar_senha(senha):

    if len(senha) < 8:
        return False

    if not re.search(r'[A-Z]', senha):
        return False

    if not re.search(r'[a-z]', senha):
        return False

    if not re.search(r'[0-9]', senha):
        return False

    return True


senha = input("Digite a senha: ")

if validar_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres,"
          "conter pelo menos uma letra maiúscula, uma letra minúscula"
          "e um número.")
