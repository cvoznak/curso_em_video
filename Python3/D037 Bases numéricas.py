n = int(input("Digite um número inteiro: "))

b = int(input("Escolha a base de conversão: 1 para binário, 2 para octal, e 3 para hexadecimal: "))

if b == 1:
    print(format(n, "b"))
elif b == 2:
    print(format(n, "o"))
elif b == 3:
    print(format(n, "x"))
else:
    print("\033[7;31m ERRO digite uma entrada válida\033[m")
