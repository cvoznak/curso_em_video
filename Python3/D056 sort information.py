np = 4  # número de pessoas a verificar/cadastrar
somaidade = 0

n = ""
i = 0
s = ""
mi = 0
mn = ""
fcont = 0

for lista in range(0, np):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    somaidade += idade
    s = sexo.upper()
    if lista == 1 and s == "M":
        mn = nome
        mi = idade
    elif s == "F" and idade < 20:
        fcont += 1
    if s == "M" and idade > mi:
        mi = idade
        mn = nome

medidade = somaidade / np
print("A média de idade do grupo é de {} anos".format(medidade))
print("O homem mais velho tem {} anos e se chama {}".format(mi, mn))
print("Ao todo são {} mulheres com menos de 20 anos.".format(fcont))
