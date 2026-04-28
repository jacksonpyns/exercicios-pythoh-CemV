import math
print('Para importar apenas uma funcionalidade o comando é: from math import ___')
print('-'*20)
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
#print('para arredondar pra cima usa math.ceil(raiz)
#print('para arredondar pra baixo usa o math.floor(raiz)
print('A raiz de {} é igual a {:.1f}'.format(num, raiz))
print('-'*20)
import random
n=random.randint(1,10)
print(n)