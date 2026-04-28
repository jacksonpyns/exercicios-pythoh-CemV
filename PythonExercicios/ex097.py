print('Faça um programa que tenha uma função chamada \033[34mescreva()\033[m, que receba um texto qualquer como parâmetro\n'
      'e mostre uma mensagem com tamanho adaptável.\nEx:\n\033[34mescreva("Olá, Mundo!")\033[m\nSaída:')
print('-'*11)
print('Olá, Mundo!')
print('-'*11)


def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


escreva ('  Gustavo Guanabara  ')
escreva('  Curso de Python no Youtube  ')
escreva('  CeV  ')