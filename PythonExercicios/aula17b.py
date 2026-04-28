teste = list()
teste.append('Jackson')
teste.append(40)
galera = list()
galera.append(teste[:]) # [:]isso faz uma cópia da lista, que é sempre o excencial
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#outro modo de colocar lista dentro de lista
pessoas = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
#          |   0  |  1   |   0  |  1   |   0   |  1    |   0   |  1    |
#          |      0      |      1      |        2      |       3       |
print(pessoas[1]) #para pegar somente um tem que ser com [] e se quiser mais da mesma estrutura coloque mais []
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade') #se quiser só os nomes é print(p[0]) ou só a idade print(p[1])

lista = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:]) #lista vai receber uma cópia do dado
    dado.clear()
for t in lista: #para mostrar somente as pessoas que tem mais de 21 anos
    if t[1] >= 21:
        print(f'{t[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{t[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')