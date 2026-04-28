print('\033[1;35mEscreva um programa que leia \033[4mdois números inteiros\033[m \033[1;35me compare-os,\n'
      'mostrando na tela uma mensagem:')
print('- O primeiro valor é maior')
print('- O segundo valor é maior')
print('- Não existe valor maior, os dois são iguais.\033[m')
print('--'*30)

n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
if n1>n2:
      print('O PRIMEIRO é maior: {}'.format(n1))
elif n1<n2:
      print('O SEGUNDO é maior: {}'.format(n2))
else:
      print('Não existe valor maior, os dois são iguais: tanto {} como {}.'.format(n1, n2))