print('Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um\n'
      'dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.')

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(0, 6),
        'jogador 2': randint(0, 6),
        'jogador 3': randint(0, 6),
        'jogador 4': randint(0, 6)}
ranking = list()
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f'{k} sorteou {v} no dado')
    sleep(1)
print('-='*16)
print(' == RANKING DOS JOGADORES ==  ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
