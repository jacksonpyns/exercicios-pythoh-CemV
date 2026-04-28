print('Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.')
print('Ex: APOS A SOPA\n' #de traz pra frente fica a mesma coisa
      'A SACADA DA CASA\n'
      'A TORRE DA DERROTA\n'
      'O LOBO AMA O BOLO\n'
      'ANOTARAM A DATA DA MARATONA')
print('-='*20)

frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
'''inverso=''
for letra in range(len(junto)-1, -1, -1):
      inverso = inverso + junto[letra]'''
print('A frase digitada foi {} e de traz pra frente fica {}.'.format(junto, inverso))
if junto == inverso:
      print('Essa frase é PALÍNDROMO!')
else:
      print('NÃO é Palíndromo.')
