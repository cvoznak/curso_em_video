l = float(input("Digite a largura da parede que deseja pintar: "))
h = float(input("Digite a altura da parede que deseja pintar: "))
a = l*h
t = a/2
print(
    "A área total a ser pintada é de {:.2f}mˆ2 e serão necessários {:.2f} litros de tinta".format(a, t))
