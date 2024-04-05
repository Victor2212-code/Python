# Exercício - Adiando execução de funções 

def soma(x, y):
    return x + y 

def multiplica(x, y):
    return x * y

# crowger
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna 

soma_com_cinco = criar_funcao(soma, 5)
multiplicar_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplicar_por_dez(10))

