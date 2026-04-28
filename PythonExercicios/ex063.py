print('Escreva um programa que leia um número \033[4mn\033[m inteiro qualquer e mostre na tela\n'
      'os \033[1mn\033[m primeiros elementos de uma Sequência de Fiboncci.\n'
      'Ex:\n0 > 1 > 1 > 2 > 3 > 5 > 8')
print('-='*24)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
      t3 = t1 + t2
      print(' > {}'.format(t3), end='')
      t1 = t2
      t2 = t3
      cont += 1
