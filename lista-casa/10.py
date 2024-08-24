a = 1
while a == 1: 
    T = input("Digite '+', '-', '*', '/' ou 'S'. \n")
    if T == "S" or T == "s":
        print("se acabou.")
        break
    else:
        x = float(input("Número A: "))
        y = float(input("Número B: "))
        if T == "+":
         print(x + y)
        elif T == "-":
            print(x - y)
        elif T == "*":
            print(x * y)
        elif T == "/":
            print(x / y)