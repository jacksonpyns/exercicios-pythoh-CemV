print('Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário\n'
      'com as seguintes informações:\n'
      '> Quantidade de notas\n'
      '> A maior nota\n'
      '> A menor nota\n'
      '> A média da turma\n'
      '> A situação (opcional)\n'
      'Adicione também as docstrings.')
print('-='*20)

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceitar vários)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return:dicionário com várias informcções sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(9, 10, 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
