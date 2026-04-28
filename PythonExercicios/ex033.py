print('Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.')

n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
n3=int(input('Terceiro valor: '))
#Verificando quem é o menor:
if n1<n2 and n1<n3:
    print('O menor valor digitado foi {}'.format(n1))
if n2<n3 and n2<n1:
    print('O menor valor digitado foi {}'.format(n2))
if n3<n2 and n3<n1:
    print('O menor valor digitado foi {}'. format(n3))
#Verficando quem é o MAIOR:
if n1>n2 and n1>n3:
    print('O MAIOR valor digitado foi {}'.format(n1))
if n2>n1 and n2>n3:
    print('O MAIOR valor digitado foi {}'.format(n2))
if n3>n1 and n3>n2:
    print('O MAIOR valor digitado foi {}'.format(n3))
