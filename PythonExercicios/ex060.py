print('Faça um programa que leia um número qualquer e mostre o seu fatorial.\n'
      'Ex:\n'
      '5! = 5x4x3x2x1 = 120')
print('-='*25)

'''from math import factorial
n=int(input('Digite um número para calcular seu Fatorial: '))
f=factorial(n)
print('Calculando {}! = {}'.format(n, f))'''

#ou

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
      print('{}'.format(c), end='')
      print(' x ' if c > 1 else' = ', end='')
      f = f * c  #f *= c
      c -= 1  #c = c - 1
print('{}'.format(f))
