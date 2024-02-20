"""
Esse módulo primo tem como objetivo:
    retornar se um número é primo ou não

    Funções disponíveis: 
        primo
"""


def primo(numero):
    """
        Essa função tem como objetivo:
          retornar se um número é primo ou não
        Parâmetros (numero):
            1 parâmetro obrigatório - do tipo númerico
    """
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return "Esse não é primo"
        else:
            return "Esse numero eh primo"
    else:
        return "Esse numero nao eh primo: numero menor ou igual a 1"


if __name__ == '__main__':
    print(primo(5))
