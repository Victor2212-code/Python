"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número inteiro: ')


# try:
#     numero_int = int(numero)
#     par = numero_int % 2 == 0
#     impar = numero_int % 2 == 1
#     if par:
#         print('Número digitado é par.')

#     elif impar:
#         print('Número digitado é ímpar.')

# except ValueError:
#     print('Número informado é inválido.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0 - 11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = input('Informe o horário atual: ')

# try:
#     horario_int = int(horario)
#     manha = horario_int >= 0 and horario_int <= 11
#     tarde = horario_int >= 12 and horario_int <= 17
#     noite = horario_int >= 18 and horario_int <= 23
    
#     if manha:
#         print('Bom dia.')
#     elif tarde:
#         print('Boa tarde.')
#     elif noite:
#         print('Boa noite.')
# except ValueError:
#     print('Horário digitado inválido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escerva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome_usuario =input('Digite seu primeiro nome: ')

nome_curto = len(nome_usuario) >= 1 and len(nome_usuario) <= 4
nome_normal = len(nome_usuario) >= 5 and len(nome_usuario) <= 6
nome_longo = len(nome_usuario) > 6

if nome_curto:
    print('nome curto.')
elif nome_normal:
    print('Nome normal.')
elif nome_longo:
    print('Nome longo.')