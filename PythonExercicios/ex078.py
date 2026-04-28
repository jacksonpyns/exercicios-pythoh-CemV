print('Faça um programa que leia 5 valores numéricos e guarde-os em uma \033[1;31mlista.\033[m\n'
      'No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')

maior = menor = 0
lista = list()
for n in range(0, 5):
      lista.append(int(input(f'Digite um valor para a posição {n}: ')))
      if n == 0:
            maior = menor = lista[n]
      else:
            if lista[n] > maior:
                  maior = lista[n]
            if lista[n] < menor:
                  menor = lista[n]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {maior} e ele está na posição ', end='')
for i, v in enumerate(lista):
      if v == maior:
            print(f'{i}... ', end='')
print()
print(f'O menor valor é {menor} e ele está na posição ', end='')
for i, v in enumerate(lista):
      if v == menor:
            print(f'{i}... ', end='')
print()
