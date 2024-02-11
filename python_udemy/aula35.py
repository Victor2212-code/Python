"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 89
numero_multiplicado = 0

while numero_multiplicado <= 10:
    print(f'{contador} X {numero_multiplicado} = {contador * numero_multiplicado}')
    numero_multiplicado += 1
    