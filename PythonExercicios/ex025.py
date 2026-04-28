print('Crie um programa que leia um nome de uma pessoa e diga se ela tem "Silva" no nome.')
print('-'*24)

n=str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem SILVA?\n{}'.format('SILVA'in n.upper()))