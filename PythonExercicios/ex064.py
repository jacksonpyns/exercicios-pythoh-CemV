print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar\n'
      'quando o usuário digitar o valor \033[31m999\033[m, que é a condição de parada. No final,\n'
      'mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)')

n = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = 0
while n != 999:
      cont += 1
      soma += n
      n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
