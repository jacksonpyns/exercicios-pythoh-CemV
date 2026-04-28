for c in range(1, 10):
    print(c)
print('FIM')
------------------------------------------------------------------------------
#ou
c = 1
while c < 10:
    print(c)
    c += 1     # c = c + 1
print('FIM')
------------------------------------------------------------------------------
for c in range(1, 5):
    n=int(input('Digite um valor: '))
print('FIM')
#ou
n=1
while n != 0: #ele vai perguntando o 'n' até digitar o valor 0, aí ele para o código
    n=int(input('Digite um avalor: '))
print('FIM')
-------------------------------------------------------------------------------
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar: [S/N]')).upper()
print('FIM')
-------------------------------------------------------------------------------
n = 1
par = 0
impar = 0 #ou par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par +1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
