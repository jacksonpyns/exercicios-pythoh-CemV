with open("arquivo_text.txt", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read() #readline() leria linha por linha, já o readlines() mostraria todas as linhas em mostrando as posições de cada linha
    #readline().splitlines() mostraria em formato de lista

print(conteudo)
