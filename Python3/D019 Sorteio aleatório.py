import random
print("Benvindo ao sorte de quem apagará a lousa")


a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

l = [a1, a2, a3, a4]

s = random.choice(l)

print("O sorteado foi {}".format(s))
