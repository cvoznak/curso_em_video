c = float(input("Informe a temperatura em \N{degree sign}C:"))
print("A temperatura de {}\N{degree sign}C corresponde a:".format(c))
print("  {}\N{degree sign}F".format((c*9/5)+32))
print("  {}K".format(c+273.15))
