print('Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e\n'
      'quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido\n'
      'informado corretamente.')
print('-='*20)

def ficha(jog='<desconhecido>', gol=0):
      print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
      g = int(g)
else:
      g = 0
if n.strip() == '':
      ficha(gol=g)
else:
      ficha(n, g)

#meu desenvolvimento funcional sem def
'''jogador = str(input('Nome do Jogador: ')).strip()
if jogador == '':
      jogador = '<desconhecido>'
gols = str(input('Número de Gols: '))
if gols == '':
      gols = '0'
elif gols != int:
      gols = '0'
print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")'''
