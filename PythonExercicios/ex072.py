print('Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero\n'
      'até vinte.\n' #sem usar if
      'Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
      n = int(input('Digite um número entre 0 e 20: '))
      if 0 <= n <= 20:
            print(f'Você digitou o número {cont[n]}')
            opcao = ' '
            while opcao not in 'NS':
                  opcao = str(input('Quer tentar de novo? [S/N]')).upper().strip()
                  if opcao == 'N':
                        break
      print('Tente novamente.')
