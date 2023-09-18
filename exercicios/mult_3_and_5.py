total = 0

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(f"A soma dos multiplos de 3 e 5 é: {total}")