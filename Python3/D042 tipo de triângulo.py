import math
print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)

l1 = float(input("Digite o comprimento do primeiro segmento: "))
l2 = float(input("Digite o comprimento do segundo segmento: "))
l3 = float(input("Digite o comprimento do terceiro segmento: "))

if l1 > abs(l2-l3) and l1 < (l2+l3) and l2 > abs(l1-l3) and l2 < (l1+l3) and l3 > abs(l1-l2) and l3 < (l1+l2):
    print("Os segmentos {}, {}, {} podem formar um triângulo".format(l1, l2, l3))
    if l1 == l2 == l3:
        print("O triângulo é equilátero")
    elif l1 == l2 and l3 != l2 or l2 == l3 and l1 != l2 or l1 == l3 and l1 != l2:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os segmentos {}, {}, {} não podem formar um triângulo".format(l1, l2, l3))
