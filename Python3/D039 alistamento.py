import datetime
y = datetime.date.today().year

g = int(input("""Qual seu genero de nascença:
[1] Masculino
[2] Feminino
"""))
if g == 1:
    print("No Brasil, seu alistamento é obrigatório")
    a = int(input("Digite o ano do seu nascimento: "))

    if (y - a) < 18:
        print("Este ano faltam {} anos para seu alistamento na junta militar.".format(
            (18-(y-a))))
    elif (y - a) == 18:
        print("Chegou a momento de você se apresentar a junta militar")
    elif (y - a) > 18:
        print("Espero que você já tenha se apresentado a junta militar, caso contrario está atrasado em {} anos.".format(y - a - 18))
elif g == 2:
    print("No Brasil, seu alistamento não é obrigatório")
