print('Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça\n'
      'para o usuário tentar descobrir qual foi o número escolhido pelo computador.')
print('O programa deverá escrever na tela se o usuário venceu ou perdeu.')
print('--='*24)

import random
from time import sleep

'''print('Vou pensar em um número entre 0 e 5...Tente adivinhar.')
n=int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
if n==random.randint(0,5):
      print('DROGA! Você me venceu! Eu pensei no {}'.format(n))
else:
      print('GANHEI! Eu pensei no número {}'.format(n))'''

computador=random.randint(0,5) #Faz o computador "Pensar"
jogador=int(input('Em qual número eu pensei? ')) #O Jogador tenta adivinhar o número
print('PROCESSANDO...')
sleep(2)
if computador==jogador:
      print('DROGA! Você pensou no {} e eu também no {}.'.format(jogador, computador))
else:
      print('GANHEI! Eu pensei no número {} e não no número {}.'.format(computador, jogador))
