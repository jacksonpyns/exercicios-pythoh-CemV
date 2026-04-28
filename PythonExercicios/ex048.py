print('Faça um programa que calcule a soma entre todos os números ímpares \n'
      'que são múltiplos de três e que se encontram no intervalo de 1 até 500.')

soma=0
cont=0
impar=0
for n in range(1, 501, 2):
      if n % 3 == 0:
            cont=cont+1 #CONTADOR
            soma=soma+n #ACOMULADOR
      impar=impar+1
print('\nDentre os {} números ímpares a soma de todos os {} ímpares divisiveis por 3 solicitados é {}'.format(impar, cont, soma))
