# Exercícios com funções

# Crie uma função que multiplica todos os argumentos 
# não nomeados recebidos 
# Retorne o total para uma variável e mostre o valor da variável 

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o números  


def multiplicador(*args):
    total = 1
    for i in args:
        total *= i
    return total

multiplica = multiplicador(1, 3, 4, 5, 6)
print(multiplica)

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par.'
    
    return f'{numero} é ímpar.'
       

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
