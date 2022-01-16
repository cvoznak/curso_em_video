c = ""
conti = h = m = 0

while True:
    if c == "N":
        break
    print("-" * 50)
    print("CADASTRE UMA PESSOA".center(50))
    print("-" * 50)
    i = int(input("Idade: "))
    if i >= 18:
        conti += 1
    while True:
        s = str(input("Sexo: [M/F] ").upper().strip())
        if s == "M":
            break
        elif s == "F":
            break
    if s == "M":
        h += 1
    elif s == "F" and i > 20:
        m += 1
    print("-" * 50)
    while True:
        c = str(input("Quer continuar? [S/N]").upper().strip())
        if c == "N":
            break
        elif c == "S":
            break
print("   FIM DO PROGRAMA   ".center(50, "="))
print(f"Total de pessoas com mais de 18 anos:{conti}")
print(f"Ao todo temos {h} homens cadastrados")
print(f"E temos {m} mulhere com menos de 20 anos")
