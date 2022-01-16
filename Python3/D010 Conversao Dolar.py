print("A cotação referencia na época da filmagem da aula era US$1.00=R$3,27")
c = float(input("Qual a cotação do dolar hoje? R$"))
r = float(input("Quantos reais você possui na carteira? R$"))
print("Você pode comprar um total de US${:.2f}".format(r/c))
