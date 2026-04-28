print('Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa\n'
      'deverá perguntar se o usuário quer ou não continuar. No final, mostre:\n'
      '\033[1;33mA)\033[m quantas pessoas tem mais de 18 anos.\n'
      '\033[1;33mB)\033[m quantos homens foram cadastrados.\n'
      '\033[1;33mC)\033[m quantas mulheres tem menos de 20 anos.\n')
print('-=-'*24)

totmais18 = homens = mulhermenosde20 = 0
while True:
      print('     CADASTRE UMA PESSOA     \n', '-'*28)
      idade = int(input('Idade: '))
      if idade >= 18:
            totmais18 += 1
      sexo = ' '
      while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
            if sexo == 'M':
                  homens += 1
            if sexo == 'F' and idade < 18:
                  mulhermenosde20 += 1
      opcao = ' '
      while opcao not in 'SN':
            opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
      if opcao == 'N':
            break
print(f'Totol de pessoas com mais de 18 anos: {totmais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Temos {mulhermenosde20} mulheres com menos de 20 anos.')