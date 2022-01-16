from random import randint
from random import choice

l = ["P", "I"]
cont = 0
re = ""

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

while True:
    if re == "PERDEU":
        break
    v = int(input("Diga um valor: "))
    e = str(input("Par ou Ímpar? [P/I] ")
            ).strip().upper()  # escolha do ussuário

    cv = randint(0, 10)  # número escolhido pelo computador
    ce = choice(l)  # escolha do computador

    soma = v + cv
    if soma % 2 == 0:
        r = "PAR"
        rc = "P"
    elif soma % 2 != 0:
        r = "ÍMPAR"
        rc = "I"
    print("--" * 15)
    print(f"Você jogou {v} e o computador {cv}. Total de {soma} deu {r}")
    print("--" * 15)
    if rc == e:
        print("Você VENCEU!")
        print("Vamos jogar novamente ...")
        cont += 1
    elif rc != e:
        re = "PERDEU"
        print(f"Você {re}!")
    print("=-" * 15)
print(f"GAME OVER! Você venceu {cont} vezes.")
