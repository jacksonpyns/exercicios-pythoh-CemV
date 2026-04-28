print('Desenvolva um programa que pergunte a distância de uma viagem em Km.')
print('Calcule o preço da passagem, \ncobrando R$0.50 por Km para viagens de até 200Km e R$0,45 para viagens longas.')
print('-'*24)

distancia=float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar sua viagem de {}Km.'.format(distancia))
'''precomenosde200=distancia*0.50
precomaisde200=distancia*0.45
if distancia<=200:
    print('O valor por km é R${:.2f}'.format(precomenosde200))
else:
    print('O valor por km é R${:.2f}'.format(precomaisde200))'''
if distancia<=200:
    preco=distancia*0.50
else:
    preco=distancia*0.45
print('O valor da sua passagem será de R${:.2f}'.format(preco))