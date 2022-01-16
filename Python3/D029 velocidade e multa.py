v = float(input("Digite sua velocidade atual: "))

if v > 80:
    print(
        """
        
        M U L T A D O ! ! ! 
        
        Você está acima do limite máximo permitido de velocidade de 80km/h!
        
        Sua multa será de R${:.2f}.
        
        """.format((v-80)*7))
else:
    print("Parabéns por dirigir de forma responsável! Tenha um bom dia e dirija com segurança!")
