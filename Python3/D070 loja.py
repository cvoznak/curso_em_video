
c = ""
soma = mil = cont = 0

print("-" * 50)
print("LOJA SUPER BARATÃO".center(50))
print("-" * 50)
while True:
    if c == "N":
        break
    n = str(input("Nome do Produto: "))
    p = float(input("Preço: R$ "))
    soma += p
    if p > 1000:
        mil += 1
    cont += 1
    if cont == 1:
        menorn = n
        menorc = p
    if menorc > p:
        menorc = p
        menorn = n
    while True:
        c = str(input("Quer continuar? [S/N] ").upper().strip())
        if c == "S" or c == "N":
            break
print("FIM DO PROGRAMA".center(50, "-"))
print(f"O total da compra foi R${soma:.2f}")
print(f"Temos {mil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {menorn} que custa R${menorc:.2f}")
