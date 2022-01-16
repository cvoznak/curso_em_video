
c = " "
soma = 0
cont = 0

while c != "N":
    n = float(input("Digite um valor: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n >= maior:
        maior = n
    elif n < menor:
        menor = n
    c = str(input("Deseja continuar [ S / N ]: ")).upper().strip()

media = soma / cont
print("A média dos {} valores digitados foi {}".format(cont, media))
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
