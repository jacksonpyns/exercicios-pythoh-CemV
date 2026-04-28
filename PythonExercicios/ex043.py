print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC\n'
      'e mostre seu status, de acordo com a tabela abaixo:')
print('- Abaixo de 18.5: Abaixo do Peso normal\n'
      '- Entre 18.5 e 25: Peso Ideal\n'
      '- 25 até 30: Sobrepeso\n'
      '- 30 até 40: Obesidade\n'
      '- Acima de 40: Obesidade Mórbida')
print('--'*25)

peso=float(input('Qual é o seu peso?(Kg) '))
altura=float(input('Qual é a sua altura?(m) '))
imc=peso/(altura**2)
print('Seu IMC foi de {:.1f} e você está '.format(imc), end='')
if imc < 18.5:
      print('ABAIXO do peso normal')
elif imc <= 18.5 and 25:
      print('no Peso IDEAL!')
elif imc <= 30:
      print('SOBREPESO.')
elif imc <= 40:
      print('em OBESIDADE!')
elif imc > 40:
      print('para MORRER com OBESIDADE MÓRBIDA!!!')
