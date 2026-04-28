print('\033[1mCrie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem\n'
      'no final, de acordo com a média atingida:\033[m')
print('- Média abaixo de 5.0:\n'
      '\033[1;41mREPROVADO\033[m')
print('- Média entre 5.0 e 6.9:\n'
      '\033[1;43mRECUPERAÇÃO\033[m')
print('- Média 7.0 ou superior:\n'
      '\033[1;44mAPROVADO\033[m')
print('--'*25)

n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2
print('\033[1;35mSuas notas foram {} e {} e a media foi {:.1f}.\033[m'.format(n1, n2, media))
if media < 5:
      print('\033[1;31mREPROVADO\033[m')
elif media >= 5 and media <= 6.9: #pode ser feito: 6.9 >= media >=5
      print('\033[1;33mRECUPERAÇÃO\033[m')
else:
      print('\033[1;34mAPROVADO\033[m')