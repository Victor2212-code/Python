# Yield from
def gen1():
    yield 1
    yield 2
    yield 3


def gen3():
    yield 7
    yield 8
    yield 9

def gen2(gen):
    
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    
g = gen2(gen1())
z = gen2(gen3())
for numero in g:
    print(numero)
for numero in z:
    print(numero)