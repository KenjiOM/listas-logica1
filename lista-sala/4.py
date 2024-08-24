n = int(input("Digite um número menor ou igual a 50: "))
if n <= 50 and n != 0:
    while n < 250:
        print(n)
        n = n * 3
else:
    print("Número Inválido")