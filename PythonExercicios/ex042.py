print('Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:')
print('- Equilátero: todos os lados iguais\n'
      '- Isósceles: dois lados iguais\n'
      '- Escaleno: todos os lados diferentes')
print('--'*25)

r1=float(input('Primeira reta: '))
r2=float(input('Segunda reta: '))
r3=float(input('Terceira reta: '))
if r1<r2+r3 and r2<r3+r1 and r3<r2+r1:
      print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
      if r1==r2==r3:
            print('EQUILÁTERO.')
      elif r1!=r2!=r3!=r1:
            print('ESCALENO.')
      elif r1==r2!=r3 or r2==r3!=r1 or r3==r1!=r2: #Aqui poderia ter colocado somente o else:
            print('ISÓSCELES.')

else:
      print('NÃO PODEM FORMAR um triângulo! Tente de novo.')
