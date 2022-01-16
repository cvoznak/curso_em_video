from math import pow, sqrt

print("Benvindo ao programa de cálculo de hipotenusa de triângulos retangulos.")
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hip = sqrt(pow(co, 2)+pow(ca, 2))
print("O valor da hipotenusa é {}".format(hip))
