nom = input("Digite seu nome: ")
sai = float(input("Digite o salário: "))

if 0 <= sai <= 400:
    salpicos = sai * 1.15
    mentos = "15%"
elif 401 <= sai <= 700:
    salpicos = sai * 1.12
    mentos = "12%"
elif 701 <= sai <= 1000:
    salpicos = sai * 1.10
    mentos = "10%"
elif 1001 <= sai <= 1800:
    salpicos = sai * 1.07
    mentos = "7%"
elif 1801 <= sai <= 2500:
    salpicos = sai * 1.04
    mentos = "4%"
elif sai > 2500:
    print("Sem aumento")
    mentos = "0%"
adedonha = round(salpicos, 2)
print(f"{nom}, {mentos} de aumento \nSeu salário atual: R$ {sai} \nSeu novo salário: R$ {adedonha}")