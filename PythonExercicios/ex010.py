print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.')
print('Considere U$1,00 = R$3,27 em 2018 e hoje está U$5,37')
n=float(input('Quanto de dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você poderia comprar U${:.2f} em 2018, e hoje U${:.2f}'.format(n, n/3.27, n/5.37))
