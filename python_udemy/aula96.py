# Módulos padrão do Pyhton(import, from, as e * )
# https://docs.python.org/3/py-modindex.html
# Inteiro - import nome_modulo
# Vantagens - você tem o namespace do módulo]
# Desvantagens: nomes grandes

# import sys

# platform = 'A minha'
# print(sys.platform)
# print(platform)


# partes - from nome_modulo import odjeto, objeto2
# Vantagens: nomes pequenos
#  Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido

# import sys as s 
# sys = 'Alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf
print(pf)

# Vantagem: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem


# má pratica - from nome_modulo import * 
# Vantagens : importa tudo de módulo
# Desvantagens: importa tudo de um módulo 
from sys import * 
print(platform)
exit()