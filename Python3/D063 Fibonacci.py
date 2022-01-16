n = int(input("Digito um número inteiro positivo diferente de zero: "))

f = 0
si = 0
sp = 0

while f != n:
    f += 1
    if f == 1:
        si = 0
        print("{}".format(si), end="->")
    elif f == 2:
        sp = 1
        print("{}".format(sp), end="->")
    elif f > 1 and f % 2 != 0:
        si = si + sp
        print("{}".format(si), end="->")
    elif f > 2 and f % 2 == 0:
        sp = sp + si
        print("{}".format(sp), end="->")
print("Essa é a série de Fibonacci até o termo que representa o número digitado.")
