print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma \033[35m\n'
      'lista composta\033[m. No final, mostre um boletim contendo a \033[35mmédia\033[m de cada um e\n'
      'permita que o usuário possa mostrar as notas de cada aluno individualemte.')

lista = list()
while True:
      nome = str(input('Nome: '))
      n1 = float(input('Nota 1: '))
      n2 = float(input('Nota 2: '))
      media = (n1 + n2)/2
      lista.append([nome, [n1, n2], media])
      opcao = ' '
      while opcao not in 'NS':
            opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
      if opcao == 'N':
            break
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
      print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
      print('-'*26)
      resp = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
      if resp == 999:
            print('FINALIZANDO...')
            break
      if resp <= len(lista) -1:
            print(f'Notas de {lista[resp][0]} são {lista[resp][1]}')
print('<<< VOLTE SEMPRE >>>')