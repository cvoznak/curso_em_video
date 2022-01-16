from datetime import date

y = date.today().year

j = 0

print("Olá! Irei analisar quantas pessoas atingiram a maior idade, com base no ano atual, {}.".format(y))

n = int(input("Digite o número de pessoas a ser analisado: "))

for c in range(0, n):
    i = int(input("Digite seu ano de nascimento: "))
    if y - i >= 21:
        j = j + 1
    else:
        j = j
print("São {} pessoas com mais que 21 anos e {} menores.".format(j, n-j))
