print("Classificarei o maior e o menor valor")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

if n1 >= n2:
    x = n1
else:
    x = n2

if x >= n3:
    y = x
else:
    y = n3

if n1 <= n2:
    k = n1
else:
    k = n2
if k <= n3:
    t = k
else:
    t = n3
print("O maior valor é {}".format(y))
print("O menor valor é {}". format(t))
