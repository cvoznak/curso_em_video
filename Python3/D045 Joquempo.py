import random

lista = [1, 2, 3]
computador = random.choice(lista)

# Style (0 (none), 1 (Bold), 4 (Underline), 7 (Negative))
# Text (30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 magent, 36 cyan, 37 grey )
# Back (40 white, 41 red, 42 green, 43 yellow, 44 blue, 45 magent, 46 cyan, 47 grey )

colors = {"red": "\033[1;31m", "clean": "\033[m", "black": "\033[7;30m"}

print("{}-=-{}".format(colors["red"], colors["clean"]) * 20)
print("  Vamos jogar?!?!?  ".center(60, "*"))
print("{}-=-{}".format(colors["red"], colors["clean"]) * 20)

print("Ready? Escolha....")
usuario = int(input("""

Faça sua escolha:
[1] Pedra
[2] Papel
[3] Tesoura

Qual sua escolha? """))

if computador == usuario:
    print("Empate")
    if computador == 1:
        print("Escolhi Pedra")
    elif computador == 2:
        print("Escolhi Papel")
    elif computador == 3:
        print("Escolhi Tesoura")
elif computador == 1 and usuario == 2 or computador == 2 and usuario == 1 or computador == 3 and usuario == 2:
    print("Ganhei")
    if computador == 1:
        print("Escolhi Pedra")
    elif computador == 2:
        print("Escolhi Papel")
    elif computador == 3:
        print("Escolhi Tesoura")
elif computador == 1 and usuario == 3 or computador == 2 and usuario == 3 or computador == 3 and usuario == 1:
    print("OK... Você ganhou!")
    if computador == 1:
        print("Escolhi Pedra")
    elif computador == 2:
        print("Escolhi Papel")
    elif computador == 3:
        print("Escolhi Tesoura")
