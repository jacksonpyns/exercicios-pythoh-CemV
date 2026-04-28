print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor')
n=int(input('Digite um número: '))
nm=n+1
ns=n-1
print('O valor digitado foi {}, o seu sucessor foi {} e o antecessor foi {}'.format(n, nm, ns))
#print('ou eu poderia ter feito apenas usando o .format(n, (n+1), (n-1))')