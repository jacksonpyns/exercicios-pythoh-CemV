from PythonExercicios.ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt") #leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    -> para criar um arquivo:
    :param nome: open vai abrir o arquivo escolhido "nome", 'wt+' é para criar o arquivo de texto
    :return:
    """
    try:
        a = open(nome, "wt+") #gravação de arquivo texto
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    """
    -> para ler um arquivo:
    :param nome: open vai abrir o arquivo "nome", 'rt' é para leitura do arquivo,
    read text (ler arquivo).
    :return:
    """
    try:
        a = open(nome, "rt")
    except:
        print("ERRO ao ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome="desconhecido", idade=0):
    """

    :param arq:
    :param nome: 'at' a significa append(colocar coisas dentro de outra coisa), então fica append text
    :param idade:
    :return:
    """
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()