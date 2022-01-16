f = input("Digite uma frase: ")

f = f.upper()

print("Na frase escrita acima a letra A aparece um total de {} vezes.".format(f.count("A")))

if f.count("A") != 0:
    print("A primeira posição onde a letra A aparece é {}.".format(f.find("A")+1))
    print("A útlima posição onde a letra A aparece é {}.".format(f.rfind("A")+1))
