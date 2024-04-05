# Try, except, else e Finally


try:
    a = 18
    b = 0
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    
except NameError:
    print('Nome b não está definido ')

except (TypeError, IndexError) as err:
    print('TypeError + IndexError')
    print('MSG', err)
    print('Nome', err.__class__.__name__)
except Exception:
    print('Erro Desconhecido')
    
print('Continuar')