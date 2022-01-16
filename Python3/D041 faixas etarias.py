import datetime

a = int(input("Digite seu ano de nascimento: "))

y = datetime.date.today().year

idade = y - a

if idade <= 9:
    print("O atleta tem {} anos e está classificado na categoria Mirim.".format(idade))
elif idade <= 14 and idade > 9:
    print("O atleta tem {} anos e está classificado na categoria Infantil.".format(idade))
elif idade <= 19 and idade > 14:
    print("O atleta tem {} anos e está classificado na categoria Junior.".format(idade))
elif idade <= 20 and idade > 19:
    print("O atleta tem {} anos e está classificado na categoria Sênior.".format(idade))
elif idade > 20:
    print("O atleta tem {} anos e está classificado na categoria Master.".format(idade))
