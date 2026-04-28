print('Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.\n'
      'O programa encerra quando ele disser que quer mostrar 0 termos.')

print('Gerador de PA')
n = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
      total = total + mais
      while cont <= total:
            print('{} > '.format(termo), end='')
            termo += r
            cont += 1
      print('PAUSA')
      mais = int(input('Quantos termos você quer mostrar a mais? '))
print('No total você pediu para acrescentar mais {} razões.'.format(total))
