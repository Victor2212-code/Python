# isinstance - para saber se objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}]
for item in lista: 
    if isinstance(item, set):
        print('SET')
        item.add(4)
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))
    
    elif isinstance(item, (int, float)):
        print('NÚMERO')
        print(item, item * 2)
    else:
        print('Outro')
        print(item)