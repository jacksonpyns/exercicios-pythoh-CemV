print('Crie um programa que leia dois valores e mostre um menu na tela:\n'
      '\n[ 1 ] somar\n'
      '[ 2 ] multiplicar\n'
      '[ 3 ] maior\n'
      '[ 4 ] novos números\n'
      '[ 5 ] sair do programa\n'
      '\nSeu programa deverá realizar a operação solicitada em cada caso.')
print('-=-'*22)

from time import sleep
n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
soma=n1+n2
mult=n1*n2
jogada=0
while not jogada == 5: #ou while jogada != 5
      sleep(0.7)
      print('\033[34m[ 1 ] somar\n\033[36m[ 2 ] multiplicar\n\033[35m[ 3 ] maior\n'
      '\033[32m[ 4 ] novos números\n\033[31m[ 5 ] sair do programa\033[m')
      jogada=int(input('>>> Qual é a sua opção? '))
      if jogada == 1:
            print('A soma de {} + {} = {}'.format(n1, n2, soma))
      elif jogada == 2:
            print('A multiplicação de {} X {} = {}'.format(n1, n2, mult))
      elif jogada == 3:
            if n1 > n2:
                  print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
            else:
                  print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
      elif jogada == 4:
            n1=int(input('Primeiro valor: '))
            n2=int(input('Segundo valor: '))
      elif jogada == 5:
            sleep(0.5)
            print('Você escolheu sair, obrigado por jogar!')
            sleep(0.5)
            print('FINALIZANDO...')
            sleep(0.5)
      else:
            print('Não existe essa alternativa! Tente novamente.')
print('FIM')
