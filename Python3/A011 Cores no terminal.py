# Usando ANSI para representar a cor
# \033[<style> <Text Color> <Back Color> m

# Style (0 (none), 1 (Bold), 4 (Underline), 7 (Negative))
# Text (30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 magent, 36 cyan, 37 grey )
# Back (40 white, 41 red, 42 green, 43 yellow, 44 blue, 45 magent, 46 cyan, 47 grey )

# print("\033[31;43mOlá mundo!\033[m")

# print("\033[7;33;44mOlá mundo!\033[m")


nome = "Caio"
cores = {"limpa": "\033[m", "azul": "\033[34m",
         "amarelo": "\033[33m", "pretoebranco": "\033[7;30m"}

print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(
    cores["azul"], nome, cores["limpa"]))
