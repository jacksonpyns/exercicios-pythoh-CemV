print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre\n'
      'quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considere após 21 anos.')
print('-='*20)

from datetime import date
atual=date.today().year
totalmaior=0
totalmenor=0
for c in range(1,8):
      nasc=(int(input('Em que ano a {} pessoa nasceu: '.format(c))))
      idade= atual - nasc
      if idade >= 21:
            totalmaior+=1
      else:
            totalmenor+=1
print('Ao todo {} pessoas são de maior e {} são de menor'.format(totalmaior, totalmenor))