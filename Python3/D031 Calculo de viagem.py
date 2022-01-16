print("Benvindo ao cálculo de custo de viagem")

d = float(input("Qual a distância total a ser viajada em km? "))

if d <= 200:
    print("Como a distância a ser viajada é {}km, será cobrado R$0.50 por km viajado, totalizando R${:.2f}.".format(d, d*0.5))
else:
    print("Como a distância a ser viajada é {}km, será cobrado R$0.45 por km viajado, totalizando R${:.2f}.".format(d, d*0.45))
