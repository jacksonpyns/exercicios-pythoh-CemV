print('Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.')
n=int(input('Digite um Valor: '))
n1=n*2
n2=n*3
n3=n**(1/2)#0.5
print('O valor digitado foi {}, \nseu dobro é {}, \nseu triplo é {}, \nsua raiz quadrada é {:.2f}'.format(n, n1, n2, n3))
