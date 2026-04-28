print('\033[1;35mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\033[m')
print('\033[1;35mO programa vai perguntar o \033[1;4;35mvalor da casa, o salário\033[m')
print('\033[1;35mdo comprador e em \033[1;4;35mquantos anos\033[m\033[1;35m ele vai pagar.\033[m')
print('\033[1;31mCalcule o valor da prestação mensal, sabendo que ela não pode exceder \033[4m30%\033[m\n'
      '\033[1;31mdo salário ou então o empréstimo será negado.\033[m')

casa=float(input('Valor da casa: R$'))
salario=float(input('Seu salário: R$'))
anos=int(input('Quantos anos de financiamento: '))
prestacao=casa/(anos *12)
minimo=salario*30/100
print('\033[1mComparando tem que pagar R${:.2f} e o mínimo é R${:.2f}'.format(prestacao, minimo))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
      print('\033[1;36mEmpréstimo APROVADO!\033[m')
else:
      print('\033[1;31mEmpréstimo NEGADO!\033[m')