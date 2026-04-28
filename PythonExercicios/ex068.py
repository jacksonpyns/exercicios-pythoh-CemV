print('Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o\n'
      'jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')

from random import randint
from time import sleep
v = 0
while True:
      jogador = int(input('Digite um valor: '))
      comput = randint(0, 10)
      soma = jogador + comput
      tipo = ' '
      while tipo not in 'PI':
            tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
      sleep(0.7)
      print('Ímpaar')
      sleep(0.7)
      print('ooouu')
      sleep(0.7)
      print('paaar')
      print(f'Você jogou {jogador} e o computador jogou {comput}. Total de {soma}', end=' ')
      print('Deu PAR' if soma %2 == 0 else 'Deu Ímpar')
      if tipo == 'P':
            if soma % 2 == 0:
                  print('Você VENCEU!')
                  v += 1
            else:
                  print('Você PERDEU!')
                  print('Vamos Jogar novamente...')
                  break
      elif tipo == 'I':
            if soma %2 != 0:
                  print('Você VENCEU!')
                  v += 1
            else:
                  print('Você PERDEU!')
                  print('Vamos Jogar novamente...')
                  break
print(f'Game Over! Você venceu {v} vezes.')