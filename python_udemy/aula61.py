'''
CPF: 764.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.: 764.824.890-70 (76482489070)
      10  9 8 7 6 5 4 3 2
*      7  4 6 8 2 4 8 9 0 
      70 36 56 12 20 32 27 0

Somar todos os resultados:
70+36+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10 
30 * 10 = 3010 
Obter o resto da divisão da conta anterior popr 11
3010 % 11 = 7 
Se o resultado anterior for maior que 9: 
    resultado é 0
contrário disso:
resultado é o valor da conta

O primeiro dígito do CPF é 7
'''

cpf = input('Digite seu cpf: ')

numero_cpf = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in numero_cpf:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito = (resultado_digito_1 * 10 ) % 11
digito = digito if digito <= 9 else 0
print(digito)