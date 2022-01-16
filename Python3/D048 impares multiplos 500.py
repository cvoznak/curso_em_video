t = 0
cont = 0

for s in range(1, 501):
    print(s)
    if s % 2 != 0:
        if s % 3 == 0:
            t += s
            cont += 1
print("A somatória dos {} números impares divisíveis por 3, entre 1 e 500 é igual a {}.".format(cont, t))
