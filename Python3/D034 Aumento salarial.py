s = float(input("Digite seu salário: R$"))

if s > 1250:
    ns = s * 1.1
else:
    ns = s * 1.15

print("Parabéns seu novo salário é R${:.2f}".format(ns))
