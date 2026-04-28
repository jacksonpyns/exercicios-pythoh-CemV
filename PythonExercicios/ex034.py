print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.')
print('Para salários superiores a R$1.250,00, calcule um aumento de 10%.')
print('Para os inferiores ou iguais, o aumento é de 15%.')
print('-'*24)

salario=float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento=(15/100*salario)
else:
    aumento=(10/100*salario)
print('Seu salário aumentou de R${:.2f} para {:.2f}'.format(salario, aumento+salario))