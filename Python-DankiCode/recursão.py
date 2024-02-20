numeroInt = 5

'''def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(10)'''
'''
1- checar se o numero não é igual a 0.
2- se não for igual a 0 nós vamos reduzir em uma unidade

5  (N-1)
  4 (5 - 1)
    3 (4 - 1)
      2 (3 - 1)
        1 (2 - 1)
           0 (1-1)
'''
'''def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        #  N - 1
        reduzirNumero(numeroInt - 1)
        return 0

reduzirNumero(5)'''


'''# Fatorial sem recursão 
def fatorialS(numero):
    fatorial = 1
    if numero == 0:# Criterio de parada
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(2))
'''

'''# Fatorial com recurçâo


def FatorialR(numero):
    if numero == 0: # Criterio de parada
        return 1
    else: # Parametro da chamada recursiva
        return numero * FatorialR(numero - 1)


print(FatorialR(4))'''

'''
5!  =  5*4!
    = 5*4*3!
    = 5*4*3*2!
    = 5*4*3*2*1!


3! = 3*2*1
   = 3 * 2!
2! = 2 * 1 
   = 2 *1!
1! = 1
0!=1

'''
