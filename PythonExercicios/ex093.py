print('Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas\n'
      'partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um \n'
      'dicionário, incluindo o total de gols feitos durante o campeonato.')
print('-='*20)

jogador = dict()
partidas = list()
tot = 0
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
if tot >= 1:
    for c in range(1, tot+1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*20)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for g, j in enumerate(jogador['gols']):
    print(f'=> Na partida {g+1}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} de gols.')
