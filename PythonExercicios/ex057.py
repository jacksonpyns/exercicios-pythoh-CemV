print('Faça um programa que leia o Sexo de uma pessoa, mas só aceite valores "M" ou "F".\n'
      'Caso esteja errado, peça a digitação novamente até ter um valor correto.')

s = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo \033[36m{}\033[m registrado com sucesso!'.format(s))