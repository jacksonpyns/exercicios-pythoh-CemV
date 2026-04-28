print('\033[1;34mFaça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:')
print('- Se ele ainda vai se alistar ao serviço militar.')
print('- Se é a hora de se alistar.')
print('- Se já passou do tempo do alistamento.')
print('Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.\033[m')
print('--'*30)

from datetime import date
ano=int(input('Ano de nascimento: '))
atual=date.today().year
alistamento=atual-18
print('Quem nasceu em {} completa {} anos em {}.'.format(ano, atual-ano, atual))
if ano < alistamento:
    print('Você já deve ter se alistado.')
elif ano == alistamento:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif ano > alistamento: #aqui poderia ser o 'else' também!
    print('Ainda faltam {} anos para o alistamento.'.format(ano-alistamento))
    print('Seu alistamento sera em {}.'. format(ano-alistamento+atual))
