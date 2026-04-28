print('Faça um programa que ajude um jogador da \033[35mMEGA SENA\033[m a criar palpites. O programa vai\n'
      'perguntar quantos jogos serão gerados e vai sortear \033[35m6 números\033[m entre 1 e 60 para cada jogo,\n'
      'cadastrando tudo em uma lista composta.')

from random import randint
from time import sleep
print('-='*15)
print('       JOGA NA MEGA SENA       \n', '-='*15)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= quant:
      cont = 0
      while True:
            num = randint(1, 60)
            if num not in lista:
                  lista.append(num)
                  cont += 1
            if cont >= 6:
                  break
      lista.sort()
      jogos.append(lista[:])
      lista.clear()
      tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
      print(f'Jogo {i+1}: {l}')
      sleep(1)
