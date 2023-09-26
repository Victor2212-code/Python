def Converter_para_Celsius(graus):
    graus = ((graus - 32) * 5/9)
    return print("O valor digitado em Celsius é: {:.4f}".format(graus))


def Converter_para_Fahrenheit(graus):
    graus = ((graus * 9/5) + 32)
    return print("O valor digitado em Fahrenheit é {:.0f}".format(graus))


graus = float(input("Digite o valor à converter: "))

while True:
    opcao = input("Escolha a conversão [1] Celsius ou [2] Fahrenheit: ")

    if opcao == "1":
        Converter_para_Celsius(graus)
        break
    else:
        Converter_para_Fahrenheit(graus)
        break
