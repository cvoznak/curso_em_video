n1 = float(input("Digite o valor em metros: "))
print("{}m é equivalente a:\n {}km (Quilômetros)\n {}hm (Hectômetros)\n {}dam (Decâmetros)\n {}dm (Decímetros)\n {}cm (Centímetros)\n {}mm (Milímetros)".format(
    n1, n1/1000, n1/100, n1/10, n1*10, n1*100, n1*1000))
