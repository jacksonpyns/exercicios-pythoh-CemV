#Tuplas
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
#print(lanche[1])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
#ou
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#esse cont é para achar a posição
#para achar a posição tbm
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#ORGANIZADO em ordem Alphabetica
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5)) #count é para mostrar quantas vezes o número 5 aparece
print(c)
print(c.index(8)) #index é para mostra em qual posição está o 8