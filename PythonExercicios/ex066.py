print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o\n'
      'usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos foram digitados\n'
      'e qual foi a soma entre eles (desconsiderando o flag).')

n = soma = cont = 0
while n != 999:
      n = int(input('Digite um valor (999 para parar): '))
      if n == 999:
            break
      cont += 1
      soma += n
print('A soma dos {} valores foi {}'.format(cont, soma))
