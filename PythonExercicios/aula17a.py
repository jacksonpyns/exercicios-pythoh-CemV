#listas recebe []
#Ex:
#lanche = ['Hamburguer', 'Suco', 'Pizza', 'Sorvete']
lanche = list(['Hamburguer', 'Suco', 'Pizza', 'Sorvete'])
lanche.append('Cooquiee') #adiciona itens na lista
lanche.insert(0, 'Cachorro Quente') #adiciona intens onde quiser, agora foi na posição do hamburguer(0)
del lanche[2] #uma maneira de eliminar um item do lanche
lanche.pop(1) #outra maneira de eliminar um item do lanche
lanche.pop() #elimina o ÚLTIMO item do lanche
lanche.remove('Pizza') #outro metodo de eliminar um item do lanche
print(lanche)

#PARA VERIFICAR SE TEM O ITEM NA LISTA LANCHE e não dar erro USA-SE:
if 'Pizza' in lanche:
    lanche.remove('Pizza')

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #vai organizar do menor para o maior
valores.sort(reverse=True) #vai organizar invertido (do maior para o menor)
len(valores) #para saber quantos itens tem
valores.append(3)
print(valores)

valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
