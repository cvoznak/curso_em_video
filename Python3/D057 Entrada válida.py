r = 0
print(r)
while r == 0:
    genero = str(input("Qual o seu gênero [M / F]: ")).strip().upper()
    if genero == "M" or genero == "F":
        r = 1
    else:
        r = 0
        print("Digite um valor válido")
