print('Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:\n'
      '\033[34mA)\033[m Quantas vezes apareceu o valor 9.\n'
      '\033[34mB)\033[m Em que posição foi digitado o primeiro valor 3.\n'
      '\033[34mC)\033[m Quais foram os números pares.')
print('-=-'*24)

#for n in range(0, 4):
   #   num = int(input('Digite um número?: '))
n = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
      print(f'O valor 3 apareceu na {n.index(3)+1} posição')
else:
      print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram ', end='')
for num in n:
      if num % 2 == 0:
            print(num, end=' ')
