nome = input("Qual é o seu nome?")
print("Prazer em te conhecer {}!".format(nome))
# {:20} escrever em 20 espaços
# {:>20} alinhamento a direita
# {:<20} alinhamento a esquerda
# {:ˆ20} alinhamento centralizado
# Se adicionarmos um simbolo ou sinal antes do indicativo de alinhamento teremos a repetição desse elemento em todas os espaços vazios.

print("Prazer em te conhecer {:20}!".format(nome))
print("Prazer em te conhecer {:>20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:=^20}!".format(nome))
