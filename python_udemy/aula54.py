'''
Faça um alista de comprar com listas 
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista 
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

import os

lista_produtos = []
while True:
        print('Selecione uma opção')
        opcao = input('[i]nserir, [a]pagar, [l]istar: ')
        
        if opcao == 'i':
            os.system('cls')
            valor = input('Valor: ')
            lista_produtos.append(valor)
            continue
        elif opcao == 'a':
            indice_str = input('Escolha um índice para apagar: ')
            
            try:
                indice = int(indice_str)
                del lista_produtos[indice]
            except ValueError:
                print('Por favor digite número int.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Erro desconhecido.')
            
        elif opcao == 'l':
            os.system('cls')
            
            if len(lista_produtos) == 0:
                print('Nada para listar.')
                
            for i, valor in enumerate(lista_produtos):
                print(i, valor)
        
        