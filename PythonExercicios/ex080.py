print('Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,\n'
      'já na posição correta de inserção (sem usar o \033[31msort()\033[m).\n'
      'No final, mostre a lista ordenada na tela.')

numeros = list()
for c in range(0, 5):
      n = int(input('Digite um número: '))
      if c == 0:
            numeros.append(n)
            print('Adicionado na posição 0 da lista...')
      elif n > numeros[len(numeros)-1]: #lido fica assim: se o número for maior doq o ultimo número da lista:
            numeros.append(n)
            print('Adicionado ao final da lista')
      else:
            pos = 0
            while pos < len(numeros):
                  if n <= numeros[pos]:
                        numeros.insert(pos, n)
                        print(f'Adicionado na posição {pos}')
                        break
                  pos += 1
print('-='*30)
print(f'Os valores digitados foram {numeros}')