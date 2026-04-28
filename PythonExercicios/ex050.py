print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles\n'
      'que forem "pares". Se o valor digitado for "ímpar, desconsidere-o\n')

soma=0
cont=0
for c in range(1, 7):
      n=int(input('Digite o {} número: '.format(c)))
      if n % 2 ==0:
            soma = soma + n
            cont = cont +1
print('A soma de todos os {} número Pares foi {}'.format(cont, soma))