print('Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.\n'
      'No final, mostre o conteúdo da estrutura na tela.')

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] <= 5:
    aluno['situacao'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

