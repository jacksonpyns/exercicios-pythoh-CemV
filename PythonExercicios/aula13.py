'''for c in range(0,6):#para dizer 'Oi' 6x
    print('Oi')
print('FIM')'''

'''for c in range(0, 6):#para contar de 0 á 5
    print(c)'''

for c in range(6, 0, -1):#para contar de 6 até 1(CONTAGEM REGRESSIVA)
    print(c)

for c in range(0, 7, 2):#ele contará de 0 até 6 pulando de 2 em 2
    print(c)

n=int(input('Digite um número: '))
for c in range(0, n+1):#ele contará até o número que eu escolher em n
    print(c)
print('FIM')

i=int(input('Início: '))#ele contará até o número que eu escolher pulando a quantidade que eu escolher
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

soma=0
for c in range(0, 4):
    n=int(input('Digite um valor: '))
    soma=soma+n #ou s+=n
print('A soma dos valores foi {}'.format(soma))
print('FIM')