print('Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.\n'
      'Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos\n'
      'palpites foram necessários para vencer.')
print('-='*24)

#JEITO QUE EU FIZ (CERTO S2)
'''import random
from time import sleep
computador=random.randint(0, 10)
vezeserrou=1
print('\033[1;36mSou seu computador...')
sleep(0.5)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(0.7)
print('Será que você consegue advinhar qual foi?\033[m')
n = int(input('Qual é seu palpite? '))
while n != computador:
    n=int(input('\033[1;31mErrou \033[1;36mKKKKKKK\033[m fala outro aí '))
    vezeserrou += 1
print('Droga, eu pensei no {}!'.format(computador))
print('Você acertou em {} tentativas. Parabéns!'.format(vezeserrou))'''

#AGORA VAI SER DO JEITO QUE O GUANABARA FEZ NA AULA:
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))