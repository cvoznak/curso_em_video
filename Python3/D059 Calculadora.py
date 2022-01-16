
m = 1
e = 0

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

while m != 0:
    print("""Escolha qual opção deseja:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do program""")
    e = int(input("                          ..."))
    if e == 1:
        print("*-*" * 40)
        print("{} + {} = {}".format(v1, v2, v1 + v2).center(120))
        print("*-*" * 40)
    elif e == 2:
        print("*-*" * 40)
        print("{} * {} = {}".format(v1, v2, v1 * v2).center(120))
        print("*-*" * 40)
    elif e == 3:
        print("*-*" * 40)
        if v1 > v2:
            print("{} > {}".format(v1, v2).center(120))
        elif v2 > v1:
            print("{} < {}".format(v1, v2).center(120))
        else:
            print("{} = {}".format(v1, v2).center(120))
        print("*-*" * 40)
    elif e == 4:
        print("Digite os novos valores: ")
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
    elif e == 5:
        m = 0
