print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, \ncalcule e mostre o comprimento da hipotenusa.')
import math
op=float(input('Comprimento do cateto oposto: '))
adj=float(input('Comprimento do cateto adjacente: '))
hip=math.sqrt(op**2+adj**2)#ou hip=math.sqrt(op, adj)
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(op, adj)))
print('A hipotenusa vai medir {:.2f}'.format(hip))
