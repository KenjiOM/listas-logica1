z = 1
simba = []
pa = []
enxada = []
media = 0
libertacao = ["sair", "Sair", "n quero mais", "cansei", "gênio, vc está livre"]
while z == 1:
    aladdin = input("Qual o seu desejo? \n")
    if aladdin in libertacao:
        print("O seu desejo é uma ordem. Muito obrigado por me libertar!🧞")
        break
    else:
        desejos = int(input("Quantos desejos você deseja? \n"))
        for a in range (1, desejos + 1):
            cvc = float(input("Digite um número: "))
            simba.append(cvc)
            media = media + cvc
            if cvc % 2 == 0:
                pa.append(cvc)
            else:
                enxada.append(cvc)
        print(f"São pares os números: {pa} \nSão ímpares os números: {enxada}")
        faixa1 = [b for b in simba if b < 0]
        faixa2 = [b for b in simba if 0 <= b <= 15]
        faixa3 = [b for b in simba if 15 <= b < 100]
        faixa4 = [b for b in simba if b >= 1000]
        faixa5 = [b for b in simba if 101 <= b < 1000] 
        print(f"A média aritmética entre eles é {media / a} \nO maior elemento é o {max(simba)} e o menor é o {min(simba)}")
        media = 0
        print(f"Faixa 1 = {faixa1}\nFaixa 2 = {faixa2}\nFaixa 3 = {faixa3}\nFaixa 4 = {faixa4}\nFaixa 5 = {faixa5}")
        print(f"Total de elementos em cada faixa:\n Faixa 1 = {len(faixa1)}\n Faixa 2 = {len(faixa2)}\n Faixa 3 = {len(faixa3)}\n Faixa 4 = {len(faixa4)}\n Faixa 5 = {len(faixa5)}")
        print(f"Total de cada faixa:\n Faixa 1 = {sum(faixa1)}\n Faixa 2 = {sum(faixa2)}\n Faixa 3 = {sum(faixa3)}\n Faixa 4 = {sum(faixa4)}\n Faixa 5 = {sum(faixa5)}")