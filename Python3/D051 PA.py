print("-=-" * 30)
print("  Progressão Aritmética  ".center(90))
print("-=-" * 30)

a1 = float(input("Digite o primeiro termo da Progressão Aritmética desejada: "))
r = float(input("Digite a razão da Progressão Aritmética desejada: "))

for c in range(1, 11):
    a = a1 + (c - 1) * r
    print(a)
