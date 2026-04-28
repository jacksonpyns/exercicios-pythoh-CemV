print('Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.\n'
      'No final do programa mostre:\n'
      '> A média de idade do grupo.\n'
      '> Qual é o nome do homem mais velho.\n'
      '> Quantas mulheres tem menos de 20 anos.')

midade=0
somaidade=0
maioridadehomem=0
nomevelho=''
qmulher=0
for p in range(1, 5):
      print('---- {} PESSOA ----'.format(p))
      nome=str(input('Nome: ')).strip()
      idade=int(input('Idade: '))
      sexo=str(input('Sexo [M/F]: ')).strip()
      somaidade+=idade
      if p == 1 and sexo in 'Mm':
            maioridadehomem = idade
            nomevelho = nome
      if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
      if sexo in 'Ff' and idade < 20:
            qmulher += 1
midade=somaidade/4
print('A média de Idade do grupo é de {:.1f} anos.'.format(midade))
print('\033[1;35mO homem mais velho tem {} anos e se chama {}.\033[m'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qmulher))