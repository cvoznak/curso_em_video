t = int(input("Digite o número para o qual gostaria de ver a tabuada: "))

for c in range(1, 11):
    print("{} x {} = {}".format(t, c, t*c))
