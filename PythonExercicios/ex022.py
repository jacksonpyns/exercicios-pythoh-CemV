print("""Crie um programa que leia o nome de uma pessoa e mostre:
> O nome com todas as letras Maiúsculas
> O nome com todas Minúsculas
> Quantas letras ao todo(sem considerar espaços).
> Quantas letras tem o primeiro nome.""")
print('-'*24)

nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em Maiúsculo: {}'.format(nome.upper()))
print('Seu nome em Minúsculo: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))