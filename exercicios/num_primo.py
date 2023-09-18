def num_primo(num):

    if (num % 2) == 0:
        return print(f"O numero {num} é par")
    else:
        return print(f"O nuemro {num} é impar")


num_primo(int(input("Digite um número:  ")))
