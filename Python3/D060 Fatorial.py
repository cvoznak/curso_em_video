f = int(input("Digite o valor para o qual deseja o fatorial: "))

j = f
f1 = f

while j != 1:
    j -= 1
    f1 = f1 * (f - j)

print("{}! = {}".format(f, f1))
