print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')

n=int(input('Digite um número: '))
cont=0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;36m', end='')
        cont=cont+1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('Por isso é um Número PRIMO!')
else:
    print('Ele NÃO é um número PRIMO.')
