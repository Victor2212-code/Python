def calcular_juros_compostos(capital_inicial, taxa_de_juros_anual, periodos_de_compound, periodo_em_anos):
    taxa_decimal = taxa_de_juros_anual / 100

    montante = capital_inicial * \
        (1 + (taxa_decimal / periodos_de_compound)
         )**(periodos_de_compound * periodo_em_anos)

    return montante


capital_inicial = float(input("Digite o capital inicial: "))
taxa_de_juros_anual = float(input("Digite a taxa de juros anual (%): "))
periodos_de_compound = int(
    input("Digite o número de vezes que os juros são compostos por ano: "))
periodo_em_anos = float(input("Digite o período de investimento em anos: "))


montante_acumulado = calcular_juros_compostos(
    capital_inicial, taxa_de_juros_anual, periodos_de_compound, periodo_em_anos)


print("O montante acumulado com juros compostos é:", montante_acumulado)
