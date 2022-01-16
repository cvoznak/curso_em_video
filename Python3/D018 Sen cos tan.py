from math import sin, cos, tan, radians
print("Programa para cálculo de sin, cos e tan.")


d = float(input("Digite um ângulo qualquer: "))
drad = radians(d)

print("Cos ({:.2f}) = {:.2f}".format(d, cos(drad)))
print("Sin ({:.2f}) = {:.2f}".format(d, sin(drad)))
print("Tan ({:.2f}) = {:.2f}".format(d, tan(drad)))
