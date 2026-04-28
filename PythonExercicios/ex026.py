print("""Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aprece a última vez.""")
print('-'*24)

frase=str(input('Digite uma frase: ')).lower().strip()
print('A frase foi: {}'.format(frase))
print('A frase contém a letra "A" {} vezes'.format(frase.count('a')))
print('A primeira letra "A" aparece na posição {}'.format(frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))