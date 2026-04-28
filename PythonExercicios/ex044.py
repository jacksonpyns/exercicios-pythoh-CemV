print('Elabore um programa que calcule o valor a ser pago por um produto,\n'
      'considerando o seu \033[1;33mpreço normal e condição de pagamento\033[m:')
print('- Á vista dinheiro/cheque: 10% de desconto\n'
      '- Á vista no cartão: 5% de desconto\n'
      '- Em até 2x no cartão: preço normal\n'
      '- 3x ou mais no cartão: 20% de juros')
print('--'*25)

preco=float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] á vista dinheiro/cheque\n'
      '[ 2 ] á vista no cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
dinheiro=preco-(preco*10/100)
cartao=preco-(preco*5/100)
#cartao2x=preco
parcela=preco+(preco*20/100)
opcao=float(input('Qual é a opção? '))
if opcao==1:
      print('Sua compra R${:.2f} ficou com o valor de 10% de desconto R${:.2f}'.format(preco, dinheiro))
elif opcao==2:
      print('Sua compra R${:.2f} ficou com o valor de 5% de desconto R${:.2f}'.format(preco, cartao))
elif opcao==3:
      print('Sua compra ficou no valor de R${:.2f} SEM JUROS.'.format(preco))
elif opcao==4:
      vezes=int(input('Quantas parcelas? '))
      parcelas=parcela/vezes
      print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(vezes, parcelas))
      print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, parcela))
else:
      print('\033[1;40mA opção selecionada não existe! Tente novamente\033[m')

