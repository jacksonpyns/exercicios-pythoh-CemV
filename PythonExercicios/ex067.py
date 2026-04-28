print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado\n'
      'pelo usuário. O programa será \033[1;31minterrompido\033[m quando o número solicitado for negativo.\n'
      'ex: -1')
print('-=-'*20)

n = 0
while True:
      n = int(input('Quer ver a tabuada de qual valor? '))
      if n < 0:
            break
      for c in range(1, 11):
            mult = n * c
            print('{} x {} = {}'.format(n, c, mult))

print('FIM')