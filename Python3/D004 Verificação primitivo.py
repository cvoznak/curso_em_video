i1 = input("Digite algo, por favor:")
print("Foi digitado algo alphanumérico - {}".format(i1.isalnum()))

print("Foi digitado algo somente alphabetic - {}".format(i1.isalpha()))

print("Foi digitado algo somente numérico - {}".format(i1.isnumeric()))

print("Foi digitado algo somente em caixa baixa - {}".format(i1.islower()))

print("Foi digitado algo somente em caixa alta - {}".format(i1.isupper()))

print("Foi digitado somente space - {}".format(i1.isspace()))

print("Foi digitado algo que pode ser impresso - {}".format(i1.isprintable()))

print(type(i1))
