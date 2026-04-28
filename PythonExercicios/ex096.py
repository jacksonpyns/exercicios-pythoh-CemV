print('Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno\n'
      'retangular (\033[35mlargura e comprimento\033[m) e mostre a área do terreno.')

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
