while True:
    t = int(input("Quer ver a tabuada de qual valor?"))
    if t < 0:
        break
    for c in range(1, 11):
        print(f"{t} x {c} = {t * c}")
print("Programa tabuada encerrado, volte sempre!")
