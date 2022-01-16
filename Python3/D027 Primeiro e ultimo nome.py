nc = input("Digite seu nome completo: ")
nc = nc.title()

lista = nc.split()

print("Seu primeiro nome é {}.".format(lista[0]))

#print("Seu último nome é {}.".format(lista[len(lista)-1]))

last = lista.reverse()
print("Seu último nome é {}.".format(lista[0]))
