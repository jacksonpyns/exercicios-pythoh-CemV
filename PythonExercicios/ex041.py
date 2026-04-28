print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta\n'
      'e mostre sua categoria, de acordo com a idade:')
print('- Até 9 anos: MIRIM\n'
      '- Até 14 anos: INFANTIL\n'
      '- Até 19 anos: JUNIOR\n'
      '- Até 20 anos: SÊNIOR\n'
      '- Acima: MASTER')
print('--'*25)

from datetime import date
nasc=int(input('Ano de Nascimento: '))
idade=date.today().year-nasc
print('\033[1;40mO atleta tem {} anos.\033[m'.format(idade))
if idade <= 9:
      print('Classificação: MIRIM')
elif idade <= 14:
      print('Classificação: INFANTIL')
elif idade <= 19:
      print('Classificação: JUNIOR')
elif idade <= 20:
      print('Classificação: SÊNIOR')
else:
      print('Classificação: \033[31mMASTER\033[m')
