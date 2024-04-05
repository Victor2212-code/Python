#Introdução às Generator functions em Pyhton
# generator = (n for n in range(10000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return 0
         

gen = generator(maximum=1000000)
for n in gen:
    print(n)