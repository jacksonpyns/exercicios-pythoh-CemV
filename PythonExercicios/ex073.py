print('Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,\n'
      'na ordem de colocação. Depois mostre:\n'
      '\033[34mA)\033[m Apenas os 5 primeiros colocados.\n'
      '\033[34mB)\033[m Os últimos 4 colocados da tabela.\n'
      '\033[34mC)\033[m Uma lista com os times em ordem alfabética.\n'
      '\033[34mD)\033[m Em que posição na tabela está o time do Corinthians.\n')
print('-=-'*24)

tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio',
          'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'EC Vitória', 'Internacional', 'Ceará',
          'Fortaleza', 'Juventude', 'Sport Recife')

coringao = ' '
alfabetico = ' '
ultimos4 = ' '
top5 = ' '
while top5 not in 'SN':
      top5 = str(input('Quer que mostre os 5 times primeiros colocados de 2025? [S/N]')).upper().strip()
      if top5 == 'N':
            break
      elif top5 == 'S':
            print(tabela[0:5])
      else:
            print('Tente novamente.')
print('---'*20)
while ultimos4 not in 'SN':
      ultimos4 = str(input('Quer saber os últimos 4 times colocados de 2025? [S/N]')).upper().strip()
      if ultimos4 == 'N':
            break
      elif ultimos4 == 'S':
            print(tabela[-4:])
      else:
            print('Tente novamente.')
print('---'*20)
while alfabetico not in 'SN':
      alfabetico = str(input('Quer ver os times do Brasileirão em ordem alfabetica? [S/N]')).upper().strip()
      if alfabetico == 'N':
            break
      elif alfabetico == 'S':
            print(sorted(tabela))
      else:
            print('Tente novamente.')
print('---'*20)
while coringao not in 'NS':
      coringao = str(input('Quer saber em qual posição está o Corinthians? [S/N]')).upper().strip()
      if coringao == 'N':
            break
      elif coringao == 'S':
            print(f'O Corinthians está na {tabela.index("Corinthians")+1} posição!')
      else:
            print('Tente novamente.')
