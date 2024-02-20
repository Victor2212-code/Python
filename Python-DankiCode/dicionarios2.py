"""dicio = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
print(dicio)

dicio["idade"] = 32

print(dicio)

dicio.update({"estado ": "Rio de Janeiro"})

print(dicio)


dicio.popitem()
print(dicio)


dicio = dicio.copy()
print(dicio)

dicio2 = dict(dicio)
print(dicio2)

dicio["idade"] = 27
print(dicio)
print(dicio)
print(dicio2)

"""
tupla = ("item1", "item2", "item3")
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)


x = 0
print(x)

#  chave: valor
dicio2 = {
    "dicio3": {
        "nome": "Ana",
        "idade": 25
    },
    "dicio4": {
        "nome": "Pedro",
        "idade": 38,

        "dicio5": {
            "nome": "Ana Julia",
            "idade": 5
        }
    }
}

print(dicio2)
