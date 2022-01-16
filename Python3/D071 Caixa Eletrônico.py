print("=" * 50)
print("BANCO CEV".center(50))
print("=" * 50)

v = int(input("Que valor você quer sacar? R$"))

n50 = v // 50
n20 = (v % 50) // 20
n10 = ((v % 50) % 20) // 10
n1 = (((v % 50) % 20) % 10) // 1


print(f"Total de {n50} cédulas de R$50")
print(f"Total de {n20} cédulas de R$20")
print(f"Total de {n10} cédulas de R$10")
print(f"Total de {n1} cédulas de R$1")
print("=" * 50)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
