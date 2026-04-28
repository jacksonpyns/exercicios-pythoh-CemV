print('Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes\n'
      'do aproveitamento de cada jogador.')

jogador = dict()
time = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nomde do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if jogador['partidas'] >= 1:
        for c in range(1, jogador['partidas']+1):
            gols.append(int(input(f'quantos gols na partida {c}? ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
    time.append(jogador.copy())
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*30)