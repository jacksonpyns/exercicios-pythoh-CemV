print('Aprimore o desafio anterior, mostrando no final:\n'
      '\033[35mA)\033[m A soma de todos os valores pares digitados.\n'
      '\033[35mB)\033[m A soma de todos os valores da terceira coluna.\n'
      '\033[35mC)\033[m O maior valor da segunda linha.')
print('-='*30)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = tercoluna = 0
for l in range(0, 3):
      for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-=-'*20)
for l in range(0, 3):
      for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if matriz[l][c] % 2 == 0:
                  spar += matriz[l][c]
      print()
print(f'A soma de todos os valores pares é {spar}')
for l in range(0, 3):
      tercoluna += matriz[l][2]
print(f'A soma dos valores da terceira colunao é {tercoluna}')
for c in range(0, 3):
      if c == 0:
            maior = matriz[1][c]
      elif matriz [1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
