print('Crie um programa que vai ler vários números e colocar em uma lista.\nDepois disso, mostre:\n'
      '\033[1;34mA)\033[m Quantos números foram digitados.\n'
      '\033[1;34mB)\033[m A lista de valores, ordenada de forma decrescente.\n'
      '\033[1;34mC)\033[m Se o valor 5 foi digitado e está ou não na lista.\n')

cont = 0
lista = list()
while True:
      lista.append(int(input('Digite um valor: ')))
      cont += 1
      r = ' '
      while r not in 'NS':
            r = str(input('Quer continuar? [S/N]')).upper().strip()
      if r == 'N':
            break
print('-='*30)
print(f'Os números digitados foram {lista}')
print(f'Foram digitados {cont} números.') #aqui eu poderia ter usado: len(lista) ao invés de cont
lista.sort(reverse=True)
print(f'Em ordem Decrescente fica {lista}')
if 5 not in lista:
      print('O valor 5 NÃO está na lista!')
else:
      print('O valor 5 foi digitado.')