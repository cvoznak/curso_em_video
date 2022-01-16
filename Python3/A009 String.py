# A string fica armazenada numerando os caracters sempre começando do 0.
# Fatiamento de string = nome variavel[indice dentro da string]
# Fatiamento de string = nome variavel [9:13] inclui cadeias de 9 até 12.
# Fatiamento de string = nome variavel [9:21:2] pula de 2 em dois
# Fatiamento de string = nome variavel [:5] vai de 0 até 4
# Fatiamento de string = nome variavel [15:] do 15 até o final
# Analise de string -> len(variavel) -> informa o número de caracters
# Analise de string -> variavel.count("o") ->conta quantas vezes aparece o caracter "o" na variável
# Analise de string -> variavel.count("o",0,13) ->conta quantas vezes aparece o caracter "o" na variável entre os caracter 0 e 12
# Analise de string -> variavel.find("deo") -> onde encontramos (qual caracter) indicado
# Analise de string -> variavel.find("casa") -> onde encontramos (qual caracter) indicado, se retornar -1 essa string não existe
# transformação -> variavel.replace("python","android") -> substitui python por android
# transformação -> variavel.upper() -> muda os caracters lower para upper
# transformação -> variavel.lower() -> muda os caracters upper para lower
# transformação -> variavel.capitalize() -> estabelece o primeiro caracter como upper e todos os outros como lower
# transformação -> variavel.title() -> Capitalize por palavra em uma frase
# transformação -> variavel.strip() -> remove os espaços no inicio e no final
# transformação -> variavel.rstrip() -> remove os espaços da direita
# transformação -> variavel.lstrip() -> remove os espaços da esquerda
# Divisão -> variavel.split() -> cria uma divisão usando os espaços gerando uma lista com as palavras
# Divisão -> "-".join(variavel) -> juntas as palavras de uma lista em uma string única com "-" de divisão

frase = "Curso em video Python"
print(frase[3:13])
print(frase[3:13:3])
print(frase[::2])

print("""jflasknflasdk fpojf pwrfpwlkf plwkrfv; alkm
as;dljas;dlvj a;slka
vv asVS;VLASF
;V AVASF;BVJ ASF;V AS;DLVKA
SF V;SLKBA;SFLBK ASDVA""")

# 3 QUOTES FAZ COM QUE SEJA IMPRESSO COMO ESTÁ MOSTRADO/DIGITADO NAS LINHAS DE COMANDO

print(frase.count("o"))
print(frase.upper().count("o"))
