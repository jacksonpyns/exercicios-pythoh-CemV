print('Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário\n'
      'e todos os dicionários em uma lista. No final, mostre:\n'
      '\033[35mA)\033[m Quantas pessoas cadastradas.\n'
      '\033[35mB)\033[m A média de idade.\n'
      '\033[35mC)\033[m Uma lista com mulheres.\n'
      '\033[35mD)\033[m Uma lista com idade acima da média.')
print('-='*20)

pessoa = dict()
lista = list()
cont = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    lista.append(pessoa.copy())
    cont += 1
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao not in 'NS':
            print('ERRO! Responda apenas com S ou N.')
    if opcao == 'N':
        media = media/cont
        break
print('-='*20)
print(lista)
print('-='*20)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulhers cadastradas foram ',end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
print()
print('D) Lista das pessoas que estão acima da média de idade:')
for m in lista:
    if m['idade'] >= media:
        print(       )
        for k, v in m.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
