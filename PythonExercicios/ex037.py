print('\033[1;32mEscreva um programa que leia um número inteiro qualquer \ne peça para o usuário escolher qual será a\n'
      'base de conversão:')
print('- 1 para binário')
print('- 2 para octal')
print('- 3 para hexadecimal\033[m')
print('--'*30)

n=int(input('Digite um número inteiro: '))
print('Escolha uma das opções para conversão: ')
print('[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opcao=int(input('Sua opção: '))
if opcao==1:
      print('\033[1;36m{} Convertido para \033[4mBINÁRIO é igual a {}.\033[m'.format(n, bin(n)[2:]))
elif opcao==2:
      print('\033[1;33m{} Convertido para \033[4mOCTAL é igual a {}.\033[m'.format(n, oct(n)[2:]))
elif opcao==3:
      print('\033[1;31{} Convertido para \033[4mHEXADECIMAL é igual a {}.\033[m'.format(n, hex(n)[2:]))
else:
      print('\033[1;40mOpção invalida, tente novamente.\033[m')
