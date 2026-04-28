print('Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um\n'
      'dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o\n'
      'salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')
print('-='*20)

import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.date.today().year - pessoa['idade']
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] == 0:
    print('-='*20)
else:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.date.today().year)
    print('-='*20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')

