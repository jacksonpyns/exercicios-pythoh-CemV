print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, \ncosseno, e tangente desse ângulo.')
import math
a=float(input('Ângulo: '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {} tem o COSSE de {:.2f}'.format(a, c))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, t))