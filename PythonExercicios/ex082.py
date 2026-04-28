print('Crie um programa que vai ler vários números e colocar em uma lista,\n'
      'Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares\n'
      'digitados, respectivamente.\nAo final, mostre o conteúdo das três listas gerados.')

lista = list()
listpar = list()
listimpar = list()
while True:
      n = int(input('Digite um número: '))
      lista.append(n)
      if n % 2 == 0:
            listpar.append(n)
      else:
            listimpar.append(n)
      resp = ' '
      while resp not in 'NS':
            resp = str(input('Quer continuar? [S/N]')).upper().strip()
      if resp == 'N':
            break
print(f'Os valores digitados foram {lista}')
print(f'Os valores PARES são {listpar}')
print(f'Os valores ÍMPARES são {listimpar}')