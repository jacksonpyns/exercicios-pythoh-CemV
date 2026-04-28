print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha\n'
      'separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.')

numeros = [[], []]
for c in range(0, 7):
      n = int(input(f'Digite o {c} número: '))
      if n % 2 == 0:
            numeros[0].append(n)
      else:
            numeros[1].append(n)
print(f'Todos os valores digitados foram {numeros}')
numeros.sort()
print(f'Os números pares foram {numeros[0]}')
print(f'Os números ímpares foram {numeros[1]}')
