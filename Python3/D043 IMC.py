peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

imc = (peso) / (altura ** 2)

if imc < 18.5:
    print("IMC = {:.2f} - Abaixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("IMC = {:.2f} - Peso ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("IMC = {:.2f} - Sobrepeso".format(imc))
elif imc >= 30 and imc < 40:
    print("IMC = {:.2f} - Obesidade".format(imc))
else:
    print("IMC = {:.2f} - Obesidade mórbida".format(imc))
