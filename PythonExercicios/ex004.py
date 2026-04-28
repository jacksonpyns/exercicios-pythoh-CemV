print('Faça um programa que leia algo pelo teclado'
      ' e mostre na tela o seu tipo primitivo'
      ' e todas as informações possíveis sobre ele.')
n1=input('Digite algo: ')
print(n1)
print('Qual tipo de classe é:\033[36m{}\033[m'.format(type(n1)))
print('Ele é um número:\033[34;45m{}\033[m'.format(n1.isnumeric()))
print('Ele é contém Letras ou Números:\033[1;34;45m{}\033[m'.format(n1.isalnum()))
print('Ele é contem apenas Letras Minusculas:\033[1;36m{}\033[m'.format(n1.islower()))
print('Ele contém apenas Letras Maisculas:{}'.format(n1.isupper()))
print('Ele contém apenas espaço:{}'.format(n1.isspace()))



