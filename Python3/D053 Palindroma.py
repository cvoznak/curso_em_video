f = str(input("Digite uma frase: "))  # frase de entrada

# remove os espaços, deixe todas as letras em minuscula
f1 = f.replace(" ", "").lower()

l = int(len(f1))  # determina o total de caracters
t = l - 1  # ajusta posicionamento devido inicio em 0

j = -1  # fator de controle dentro do laço

for l in range(0, l):
    if f1[l] == (f1[(t)-l]):
        j = j + 1
    else:
        j = j
print(j)
print(l)
if j == l:
    print("A frase é um palindromo.")
else:
    print("A frase não é um palindromo.")
