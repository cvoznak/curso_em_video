nome = str(input("Digite seu nome completo: "))

print("Seu nome em maiúsculas é {}.".format(nome.upper()))

print("Seu nome em minúsculas é {}.".format(nome.lower()))

semespaconome = nome.strip()
listanome = semespaconome.split()
semespaconome = "".join(listanome)

print("Seu nome tem ao todo {} letras.".format(len(semespaconome)))

primeironome = listanome[0]
print("Seu primeiro nome é {} e ele tem {} letras.".format(
    primeironome, len(primeironome)))

# prova real pelo método apresentado pelo Guanabara
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")))
