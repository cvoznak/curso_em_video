from typing import Container


soma = 0
cont = 0

for c in range(0, 6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma += n
        cont = 1 + cont

print("A somatória dos {} números pares é {}.".format(cont, soma))
