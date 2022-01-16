n = input("Digite um número que esteja contido entre 0 e 9999: ")

# math
ni = int(n)
milhar = ni // 1000
centena = (ni % 1000)//100
dezena = ((ni % 1000) % 100)//10
unidade = ((ni % 1000) % 100) % 10

#u = n // 1 % 10
#d = n // 10 % 10
#c = n // 100 % 10
#m = n // 1000 % 10

print("unidade: {}".format(unidade))
print("dezena:  {}".format(dezena))
print("centena: {}".format(centena))
print("milhar:  {}".format(milhar))

# str
if len(n) == 4:
    print("unidade: {}".format(n[3]))
    print("dezena:  {}".format(n[2]))
    print("centena: {}".format(n[1]))
    print("milhar:  {}".format(n[0]))
elif len(n) == 3:
    print("unidade: {}".format(n[2]))
    print("dezena:  {}".format(n[1]))
    print("centena: {}".format(n[0]))
    print("milhar:  {}".format("0"))
elif len(n) == 2:
    print("unidade: {}".format(n[1]))
    print("dezena:  {}".format(n[0]))
    print("centena: {}".format("0"))
    print("milhar:  {}".format("0"))
elif len(n) == 1:
    print("unidade: {}".format(n[0]))
    print("dezena:  {}".format("0"))
    print("centena: {}".format("0"))
    print("milhar:  {}".format("0"))
