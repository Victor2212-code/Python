"""
Exercicio ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados 
    Exiba: 
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços 
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        a última letra do seu nome é {letra}
SE nada for digitado em nome ou idade:
exiba "Desculpe, você deixou campos vazios."
"""

nome_usuario = input('Digite seu nome: ') 
idade_usuario = input('Digite sua idade: ')

if nome_usuario and idade_usuario:
        print(f'Seu nome é {nome_usuario}')
        print(f'Seu nome invertido é {nome_usuario[::-1]}')
        if ' ' in nome_usuario:
            print('Seu nome contém espaços')
        else:
            print('Seu nome não contém espaços.')
        print(f'Seu nome tem {len(nome_usuario.replace(" ", ""))} letras')
        print(f'Primeira letra do seu nome é {nome_usuario[0]}')
        print(f'A ultima letra é {nome_usuario[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')