print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.\n'
      'Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores\n'
      'únicos digitados, em ordem crescente.')

listanum = list()
while True:
      n = int(input('Digite um valor: '))
      if n not in listanum:
            listanum.append(n)
            print('Valor adicionado com sucesso...')
      else:
            print('Valor duplicado! Não vou adicionar...')
      opcao = ' '
      while opcao not in 'NS':
            #print('Tente novamente.')
            opcao = str(input('Quer continuar? [S/N]')).upper().strip()
      if opcao == 'N':
            break
print('-='*30)
print(f'Os valores digitados foram {listanum}')
listanum.sort()
print(f'Os valores em ordem crescente fica {listanum}')