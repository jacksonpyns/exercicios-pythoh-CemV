print('Escreva um programa que leia a velocidade de um carro.')
print('Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.')
print('A multa vai custar R$7,00 por cada Km acima do limite.')
print('-'*24)

from time import sleep
velocidade=float(input('Qual é a velocidade atual do carro? '))
multa=(velocidade-80)*7
if velocidade<=80:
    print('Sua velocidade {}Km/h está aprovada!'.format(velocidade))
else:
    print('VOCÊ FOI MULTADO!')
    sleep(0.5)
    print('Sua velocidade atual {}Km/h ultrapassou o limite de 80km/h'.format(velocidade))
    sleep(0.5)
    print('Você íra ter que pagar uma multa no valor de R${:.2f}'.format(multa))