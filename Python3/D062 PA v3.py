ptermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))

p10 = ptermo + 9 * razao

c = ptermo
t = 0
k = 1
w = 10
p = 1

while p != 0:
    t += 1
    if t <= 10:
        c = ptermo + ((t-1) * razao)
        print("{}".format(c), end="->")
    elif t > 10:
        p = int(input("Gostaria de ver mais quantos termos?"))
        k = p
        while k != 0:
            k = k - 1
            w += 1
            c = ptermo + ((w-1) * razao)
            print("{}".format(c), end="->")
print("Foi mostrado um total de {} termos da PA".format(w))
