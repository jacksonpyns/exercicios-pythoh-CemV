print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto')
p=float(input('Qual é o preço do produto? R$'))
d=p-(p*0.05)#print('poderia ser também p-(p*5/100)')
print('O produto era R${:.2f} e seu novo valor com 5% de desconto é R${:.2f}'.format(p, d))