# try, except else e finally
try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu zeros')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')    

else:
    print('Não deu erro')

finally:
    print('Fechar Arquivo')
