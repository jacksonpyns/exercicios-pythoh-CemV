def calcular_velocidade_media(distancia: float, tempo: float, unidade_medida="km/h"):
    #Código da nossa função
    velocidade_media = distancia / tempo
    # exibir o resultado
    print(f"A velocidade média é {velocidade_media}{unidade_medida}")


#solicitar distância e tempo
dist_digitado = float(input("Digite a distância percorrida: "))
tempo_digitado = float(input("Digite o tempo da viagem: "))
'''velocidade_media = distancia / tempo
# exibir o resultado   #peguei essas funções e subi pra área do def
print(f"A velocidade média é {velocidade_media}")'''
calcular_velocidade_media(dist_digitado, tempo_digitado) #nao preciso colocar o valor "unidade_medida" a menos que eu vá trocar a unidade de medida

# Função com ARGUMENTOS VARIÁVEIS
def exibe_promocao(*clientes):
    for cliente in clientes:
        print(f"Olá, {cliente}!\nQueremos te avisar que a nova X-WING está em promoção!")


lista_clientes = ["Luke", "Princesa Leia", "Mestre Yoda"]
exibe_promocao(*lista_clientes)
#exibe_promocao("Princesa Leia")
#exibe_promocao("Mestre Yoda")

# Funções com argumentos variáveis NOMEADOS(**KWARGS)
def exibe_ficha(**dados):
    print("-----FICHA-----")
    print(dados["nome"])
    print(dados["estado_civil"])
    #for dado in dados:
    #    print(f"{dado}")

exibe_ficha(nome="Dino da Silva", estado_civil="Casado")
#mas se caso o usuário tente colocar a chave idade, não irá funcionar, então:
def exibe_ficha(**dados):
    print("-----FICHA-----")
    for chave, valor in dados.items(): # o .items() é do dicionário
        print(f"{chave.upper()} - {valor}")

ficha_cliente = {
    "nome": "Dino da Silva Sauro",
    "estado civil": "casado",
    "camisa": "xadrez",
    "filhos": True
}

exibe_ficha(**ficha_cliente)