from random import randint

computador = randint(1, 10)

c = 0
cont = 1

while c == 0:
    usuario = int(input("Tente adivinhar qual número escolhi entre 0 e 10! "))
    if usuario == computador:
        c = 1
    else:
        c = 0
        cont += 1
print("Bingo! Você acertou em {} palpites...".format(cont))
