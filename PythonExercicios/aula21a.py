 #help()
def contador(i, f, p):
     """
     -> Faz uma contagem e mostra na tela.
     :param i: início da contagem
     :param f: fim da contagem
     :param p: passo da contagem
     :return: sem retorno
     Função criada por Jackson!
     """
     c = i
     while c <= f:
         print(f'{c} ', end='')
         c += p
     print('Fim!')

help(contador)

#parâmetros opcionais
def somar(a=0, b=0, c=0):#se por acaso lá embaixo no programa principal nao for colocado o 'c' ele vai receber 0
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)

#escopo de variáveis
def funcao():
    n1 = 4  #local
    print(f'N1 dentro do escopo local vale {n1}')


n1 = 2    #global
funcao()
print(f'N1 fora vale {n1}')

#retorno de valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
