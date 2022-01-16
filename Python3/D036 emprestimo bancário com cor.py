from math import ceil

cores = {"limpa": "\033[m", "red": "\033[1;31m", "neg": "\033[7; 30m"}

print("{}-=-{}".format(cores["red"], cores["limpa"]) * 20)
print("  Desafio 036  ".center(60, "*"))
print("{}-=-{}".format(cores["red"], cores["limpa"]) * 20)

print("Por favor complete as informações abaixo.")
# valor da casa
c = float(input("Qual o valor da casa que você deseja adquirir: R$ "))
s = float(input("Qual seu salário mensal? R$ "))  # salario do comprador
# prazo (anos)
pa = float(input("Deseja financiar o pagamento do imóvel em quantos anos? "))

# enunciado pede para considerar sem juros

pm = pa * 12  # prazo para financiar em meses
cm = c / pm  # valor da parcela mensal

print("O valor do imóvel a ser financiado é de R${:.2f}.".format(c))
print(
    """O prazo desejado para o finciamento é de {:.1f} anos, 
ou seja, {:.0f} meses.""".format(pa, pm))

po = (cm * 100) / s  # porcentagem do salário mensal

si = (cm * 100) / 30  # salário ideal

cmmax = s * 0.3  # parcela máx com base no salário

pmmin = c / cmmax  # prazo ideal em meses
pamin = pmmin / 12  # prazo ideal em anos

if cm > (s * 0.3):
    print("""Infelizmente não foi possível aprovar seu financiamento, 
pois sua parcela mensal seria de R${:.2f}, o que representa 
{:.2f}% do seu salário mensal,
uma fração maior que 30% do seu salário.

Somente poderiamos aceitar seu financiamento caso 
seu salário fosse de R${:.2f} ou o imóvel teria que 
ser financiado em {} meses, {} anos""".format(cm, po, si, ceil(pmmin), ceil(pamin)))
else:
    print("Parabéns seu financiamento foi aprovado!")
    print("""Informações do financiamento:
    Valor mensal R${:.2f}""".format(cm))
