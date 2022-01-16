pn = float(input("Digite o valor normal do produto: "))

c1 = int(input("Digite 1 para pagamento à vista, 2 para pagamento em 2x no cartão e 3 para pagamento em 3x ou mais: "))

if c1 == 1:
    c2 = str(input(
        "Digite A para pagamento em dinheiro ou cheque ou B para pagamento no cartão").upper())
    if c2 == "A":
        print("Devido a condição escolhida o produto teve um desconto de 10% e seu valor final será R${:.2f}.".format(
            pn * 0.9))
    elif c2 == "B":
        print("Devido a condição escolhida o produto teve um desconto de 5% e seu valor final será R${:.2f}.".format(
            pn * 0.95))
elif c1 == 2:
    print(
        "Será concedido um benefício devida a condição de pagamento escolhida e poderá efetuar o pagamento em 2x no cartão considerando o valor à vista R${:.2f}.".format(pn))
elif c1 == 3:
    print("Devido a forma de pagamento escolhida o valor do produto sofrerá um acréscimo de 20% de juros, totalizando o valor final de R${:.2f}.".format(
        pn * 1.2))
