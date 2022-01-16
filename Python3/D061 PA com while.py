ptermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))

p10 = ptermo + 9 * razao

c = ptermo
t = 0

while t != 10:
    t += 1
    c = ptermo + ((t-1) * razao)
    print("{}".format(c), end="-> ")
