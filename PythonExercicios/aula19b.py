estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #tem que fazer uma cópia para não dar erro, e só pode ser feito cópias [:] em listas
for e in brasil: #esse for é da lista
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

    for v in e.values():
        print(v, end=' ')
    print()