c = input("Digite o nome da cidade: ")
c = c.strip()
c = c.lower()
c = c.title()

if c.find("Santo", 0) == 0:
    print("O nome dessa cidade começa com Santo.")
else:
    print("O nome dessa cidade não começa com Santo")

#print(c[:5] == "Santo")
