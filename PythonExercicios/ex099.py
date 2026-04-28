print('Faça um programa que tenha uma função chamada \033[35mmaior()\033[m, que receba vários parâmetros com valores\n'
      'inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.')

from time import sleep

def maior(*num):
      cont = maior = 0
      print('-='*30)
      print('\nAnalisando os valores passados...')
      for valor in num:
            print(f'{valor} ', end='')
            sleep(0.4)
            if cont == 0:
                  maior = cont
            else:
                  if valor > maior:
                        maior = valor
            cont += 1
      print(f'Foram informados {cont} valores ao todo.')
      print(f'O maior valor inforamdo foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()