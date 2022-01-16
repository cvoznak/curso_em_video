# for c in range(0, 5):
#    print("Oi")

# for c in range(0, 5):
#    print(c)

# for c in range(0, 10, 3):
#    print(c)

for c in range(0, 20):
    if c % 2 == 0:
        print("{} é par".format(c))
    else:
        print("{} é impar".format(c))

for p in range(10, 0, -1):
    print(p)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f, p):
    print(c)

s = 0
for t in range(0, 4):
    n = int(input("Digite um valor: "))
    s = s + n
print("O somatório de todos os valores foi {}.".format(s))

k = 0
for j in range(0, 4):
    l = int(input("Digite um valor: "))
    k += l
print("O somatório de todos os valores foi {}".format(k)")
