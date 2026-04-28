print('Crie um programa que leia vário números inteiros pelo teclado. No final da execução, mostre a\n'
      'média entre todos os valores e qual foi o \033[31mmaior\033[m e o \033[31mmenor\033[m valores lidos.\n'
      'O programa deve perguntar ao usuário se ele quer ou não \33[36mcontinuar\033[m a digitar valores.')


start = 'S'
media = cont = soma = maior = menor = 0
while start in 'Ss':
      n = int(input('Digite um número: '))
      cont += 1
      soma += n
      if cont == 1:
            maior = menor = n
      else:
            if n > maior:
                  maior = n
            if n < menor:
                  menor = n
      start = str(input('Quer continuar? [S/N]')).upper().strip()[0]

media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))