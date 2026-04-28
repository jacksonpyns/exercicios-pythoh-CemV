print('Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o\n'
      'usuário vai continuar. No final, mostre:\n'
      '\033[1;33mA)\033[m Qual é o total gasto na compra.\n'
      '\033[1;33mB)\033[m Quantos produtos custam mais de R$1000.\n'
      '\033[1;33mC)\033[m Qual é o nome do produto mais barato.')
print('-=-'*20)

print('       LOOJÃO DO JACK       \n', '--'*13)

totgasto = prod1000 = menor = cont = 0
barato = ''
while True:
      produto = str(input('Nome do Produto: ')).strip()
      preco = float(input('Preço: R$'))
      cont += 1
      totgasto += preco
      if preco >= 1000:
            prod1000 += 1
      if cont == 1:
            menor = preco
            barato = produto
      else:
            if preco < menor:
                  menor = preco
                  barato = produto
      opcao = ' '
      while opcao not in 'SN':
            opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
      if opcao == 'N':
            break
print(f'Total gasto foi de R${totgasto:.2f}')
print(f'{prod1000} Produtos custão mais de R$1000')
print(f'O produto mais barato é o {barato} e custa R${menor:.2f}')