b = 1
for a in range(1, 200):
    if a % 4 == 0:
        print(a)
        b += 1
print(f"Quantidade de números divisíveis por 4: {b}")