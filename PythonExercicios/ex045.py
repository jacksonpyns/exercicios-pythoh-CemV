print('Crie um programa que faça o computador jogar \033[1;36mJokenpô\033[m com você.')

import random
from time import sleep
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
itens= ('Pedra', 'Papel', 'Tesoura')
jogada=int(input('Qual é a sua jogada? '))
computador = random.randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*20)
print('O Jogador escolheu {}'.format(itens[jogada]))
print('O Computador escolheu {}'.format(itens[computador]))
'''if jogada == computador:
      print('EMPATE!!!')
elif jogada == 0 and computador == 1 or jogada == 1 and computador == 2 or jogada == 2 and computador == 0:
      print('Computador Venceu!')
elif jogada == 1 and computador == 0 or jogada == 2 and computador == 1 or jogada == 0 and computador == 2:
      print('Jogador VENCEU!')
else:
      print('Não existe essa jogada! Tente novamente.')'''
if computador == 0:
      if jogada == 1:
            print('Jogador Venceu!')
      elif jogada == 2:
            print('Computador Venceu!')
      elif jogada == 0:
            print('EMPATE!')
      else:
            print('Inválido. Tente novamente.')
elif computador == 1:
      if jogada == 2:
            print('Jogador Venceu!')
      elif jogada == 0:
            print('Computador VENCEU!')
      elif jogada == 1:
            print('Empate!')
      else:
            print('Inválido. Tente novamente.')
elif computador == 2:
      if jogada == 0:
            print('Jogador Venceu!')
      elif jogada == 1:
            print('Computador Venceu!')
      elif jogada == 2:
            print('Empate!')
      else:
            print('Inválido. Tente novamente.')
else:
      print('Inválido. Tente novamente.')