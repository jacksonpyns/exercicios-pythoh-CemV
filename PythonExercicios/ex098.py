print('Faça um programa que tenha uma função chamada \033[35mcontador()\033[m, que receba três parâmetros:\n'
      'início, fim e passo. Seu programa tem que realizar três contagens através da função criada:\n'
      '\033[35mA)\033[m De 1 até 10, de 1 em 1\n'
      '\033[35mB)\033[m De 10 até 0, de 2 em 2\n'
      '\033[35mC)\033[m Uma contagem personalizada')
print('~'*20)

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
