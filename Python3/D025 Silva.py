n = input("Digite seu nome completo: ")
n = n.strip()
n = n.title()

if n.find("Silva") != -1:
    print("""É um prazer conhecer mais um integrante da família Silva.
Muito prazer em te conhecer {}""".format(n))
else:
    print("Muito prazer {}".format(n))

#format("silva" in n.lower())
