print('Desenvolva um programa que leia o comprimento de três retas \ne diga ao usuário se elas podem ou não formar um triangulo.')
r1=float(input('\033[1;31mPrimeira reta: \033[m'))
r2=float(input('\033[1;33mSegunda reta: \033[m'))
r3=float(input('\033[1;34mTerceira reta: \033[m'))
triangulo=r1<r2+r3 and r2<r3+r1 and r3<r1+r2
if triangulo:
    print('\033[35mAs retas {}, {} e {} PODEM formar um triângulo\033[m'.format(r1, r2, r3))
else:
    print('\033[1;41mAs retas {}, {} e {} NÃO PODEM formar um triângulo\033[m'.format(r1, r2, r3))
