n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print("O primeiro valor digitado {} é o maior e o segundo valor digitado {} é o menor.".format(n1, n2))
elif n2 > n1:
    print("O segundo valor digitado {} é o maior e o primeiro valor digitado {} é o menor.".format(n2, n1))
else:
    print("Não existe valor maior, os dois são iguais")
