print("-=-" * 30)
print("  Progressão Aritmética  ".center(90))
print("-=-" * 30)

a1 = int(input("Digite o primeiro termo da Progressão Aritmética desejada: "))
r = int(input("Digite a razão da Progressão Aritmética desejada: "))
t = int(input("Digite o número de termos da progressão: "))
n = t + 1  # número de termos
an = a1 + (n-1)*r

for c in range(a1, an, r):
    print(c)

for c in range(a1, an, r):
    print("{}".format(c), end="-> ")
print("Acabou")
