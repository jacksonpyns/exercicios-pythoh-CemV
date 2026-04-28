print('Crie um programa que mostre na tela todos os \n'
      'números pares que estão no intervalo entre 1 e 50.')

for n in range(2, 51, 2):
    #if n % 2 == 0: #pode ser feito dessa maneira também! porém o outro print não funciona direito
    print(',', end='')
    print(n, end=' ')

print('\nEsses são os números Pares!')