n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

m = (n1 + n2) / 2

if m < 5:
    print("Sua média foi {:.1f}, infelizmente você foi reprovado.".format(m))
elif m >= 5 and m <= 6.9:
    print(
        "Atenção, sua média foi {:.1f}, você deverá fazer recuperação.".format(m))
else:
    print("Parabéns!!! Sua média foi {:.2f}, você foi aprovado.".format(m))
