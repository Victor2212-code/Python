def e_palindromo(texto):
    texto = texto.lower()  # Converter para minúsculas para tornar a verificação de palíndromo insensível a maiúsculas e minúsculas
    texto = texto.replace(" ", "")  # Remover espaços em branco
    inverso = texto[::-1]  # Inverter o texto
    return texto == inverso

frase = input("Digite uma palavra ou frase: ")

if e_palindromo(frase):
    print(f"'{frase}' é um palíndromo.")
else:
    print(f"'{frase}' não é um palíndromo.")
