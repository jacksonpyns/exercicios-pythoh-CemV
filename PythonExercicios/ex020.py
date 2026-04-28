print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. \nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
from random import shuffle
al1=str(input('Aluno 1: '))
al2=str(input('Aluno 2: '))
al3=str(input('Aluno 3: '))
al4=str(input('Aluno 4: '))
lista=[al1, al2, al3, al4]
shuffle(lista)
print('A ordem sorteada foi \n{}'.format(lista))
