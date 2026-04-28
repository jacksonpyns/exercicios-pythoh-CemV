print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')
print('-'*60)

num=int(input('Me diga um número qualquer: '))
resultado=num%2
if resultado==0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))