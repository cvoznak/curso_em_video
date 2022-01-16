frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)

inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")

print("O inverso de {} é {}.".format(junto, inverso))

# é possível fazer o inverso com o fatiamento de str, como mostrado abaixo:
inversofat = junto[::-1]
print(inversofat)
