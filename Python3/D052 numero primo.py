print("-=-" * 30)
print("  Número primo  ".center(90))
print("-=-" * 30)

j = 0
p = int(input("Digite o número que deseja verificar se é primo: "))

for c in range(p, 0, -1):
    if p % c == 0:
        print("O número {} é divisível por {}.".format(p, c))
        j = j + 1
if j > 2:
    print("O número não é primo")
else:
    print("O número é primo, pois somenete é divisível por ele mesmo, por 1 e seus opostos negativos.")
