import json
dicionario = {
    "nome": "Python",
    "missão": "Ser incrível!"
}

conteudo = json.dumps(dicionario, ensure_ascii=False, indent=4)
# ensure_ascii=False faz com que o texto continue com acentuação
# indent=4 faz com que o texto comece com 4 linhas de espaços vazios
# dumps trasforma o conteudo do arquivo em s que é str
with open("arquivo.json", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(conteudo)

print("Arquivo gerado corretamente!")