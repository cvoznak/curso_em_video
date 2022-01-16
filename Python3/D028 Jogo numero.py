import random
lista = [0, 1, 2, 3, 4, 5]
e = random.choice(lista)

print("""Vamos brincar de adivinhar!!!
Irei escolher um número entre 0 e 5, e você terá que adivinhar minha escolha!

Preparado?""")

a = int(input("Qual número você acha que eu escolhi?"))

if a == e:
    print("Parabéns você acertou")
else:
    print("Bééééééééé errado")
