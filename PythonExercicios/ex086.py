print('Crie um programa que cria uma matriz de \033[35mdimensão 3x3\033[m e preencha com valores lidos pelo teclado.\n'
      '  __________      Ex:\n'
      '0 |__|__|__|      [ 1 ][ 2 ][ 3 ]\n'
      '1 |__|__|__|      [ 4 ][ 5 ][ 6 ]\n'
      '2 |__|__|__|      [ 7 ][ 8 ][ 9 ]\n'
      '   0  1  2 \n'
      'No final, mostre a matriz na tela, com a formatação correta.')
print('-=-'*20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
      for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-=-'*20)
for l in range(0, 3):
      for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='') #:^5 faz com que fique com 5 espaços centralizado
      print()
