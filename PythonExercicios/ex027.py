print(""""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro= Ana
Último= Souza""")
print('-'*24)

n=str(input('Digite seu nome completo: '))
print('O Primeiro nome é: {}.'.format(n.split()[0]))
print('O Último nome é: {}.'.format(n.split()[-1]))