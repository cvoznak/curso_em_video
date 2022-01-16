print("Se desejar encerrar o programa digite 999")

n = 0
soma = 0
cont = 0

while n != 999:
    n = int(input("Digite um número inteiro: "))
    if n != 999:
        soma += n
        cont += 1
    else:
        soma = soma
        cont = cont
print("Foram digitados {} números inteiros excluindo 999, e a somatória de todos os números digitados foi {}".format(cont, soma))
