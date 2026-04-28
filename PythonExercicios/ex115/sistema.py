from PythonExercicios.ex115.lib.interface import *
from PythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq): #se retirar o not, usar o else
    criarArquivo(arq)
    '''print("Aquivo encontrado com sucesso!")
else:
    print("Arquivo não encotrado!")
    criarArquivo(arq)'''

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar nova Pessoas", "Sair do Sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)

    elif resposta == 2:
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho("Saindo do Sistema... Até logo!")
        break
    else:
        print("\033[1;31mERRO! Digite uma opção válida.\033[m")
    sleep(1)

