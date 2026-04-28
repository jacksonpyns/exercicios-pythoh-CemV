#DICIONÁRIO
#dados = dict()
dados = {'Nome' : 'Jackson' , 'Idade' : '19'}
print(f'O {dados["Nome"]} tem {dados["Idade"]} anos.')
print(dados['Nome'])
print(dados['Idade'])
#para acrescentar mais elementos não se usa o append é só por ex:
dados['Sexo']='M' #aqui é para adicionar itens dentro da lista do dicionário
print(dados['Sexo'])
for k in dados.keys(): #aqui pode ser o .keys e .values
    print(k)

for k, v in dados.items():
    print(f'{k} = {v}')

#para remover um elemento é:
del dados['Idade']

filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'}
#filme
# |'Star Wars' | 1977 | George Lucas |
# |   titulo   |  ano |    diretor   |
print(filme.values()) #aqui ele pega apenas as partes de cima
print(filme.keys()) #pega a parte de baixo
print(filme.items()) #pega tudo, parte de cima e de baixo

#para colocar dicionários dentro de lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) #vai mostrar Rio de Janeiro