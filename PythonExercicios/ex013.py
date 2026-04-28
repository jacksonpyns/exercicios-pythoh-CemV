print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento!')
s=float(input('Qual é o salário do Funcionário? R$'))
aumento=s+(s*15/100)
print('O salário era R${:.2f} e com o aumento de 15% ficou R${:.2f}'.format(s, aumento))
