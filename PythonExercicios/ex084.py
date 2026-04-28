print('Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:\n'
      '\033[35mA)\033[m Quantas pessoas foram cadastradas.\n'
      '\033[35mB)\033[m Uma listagem com as pessoas mais pesadas.\n'
      '\033[35mC)\033[m Uma listagem com as pessoas mais leves.')
print('-='*30)

lista = list()
dados = list()
cont = maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'A lista é {lista}')
print(f'Foram cadastrados {cont} pessoas.')
print(f'O maior peso foi {maiorpeso}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maiorpeso:
        print(p[0])
print(f'O menor peso foi {menorpeso}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menorpeso:
        print(p[0])

