from logging import addLevelName

print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. \nFaça um programa que ajude ele, \nlendo o nome deles e escrevendo o nome do escolhido.')
import random
al1=str(input('Primeiro aluno: '))
al2=str(input('Segundo aluno: '))
al3=str(input('Terceiro aluno: '))
al4=str(input('Quarto aluno: '))
lista=[al1, al2, al3, al4]
escolhido=random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
print('Entre os alunos {},{},{} e {} o escolhido foi {}'.format(al1, al2, al3, al4, random.choice([al1, al2, al3, al4])))