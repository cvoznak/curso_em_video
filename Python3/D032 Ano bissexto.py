a = int(input("Digite o ano que quer analisar: "))

if a % 4 == 0:
    print("O ano {} é bissexto".format(a))
elif a % 400 == 0:
    print("O ano {} é bissexto".format(a))
elif a % 100 == 0:
    print("O ano {} é bissexto".format(a))
else:
    print("O ano {} não é bissexto.".format(a))
