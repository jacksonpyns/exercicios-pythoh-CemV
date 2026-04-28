def aumentar(n = 0, taxa = 0, formato=False):
    '''

    :param n: Preço, será o valor que o usuário digitar
    :param taxa: Porcentagem que o usuário digitar
    :param formato: Falso por padrão, ele continuara sem formatação, então deve-se colocar "True" lá
    :return: Vai retornar o valor obtido, se estiver sem a formatação, ele colocará automaticamente
    '''
    res = n + (n * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(n = 0, taxa = 0, formato=False):
    res = n - (n * taxa/100)
    return res if formato == False else moeda(res)


def dobro(n = 0, formato=False):
    res = n*2
    return res if not formato else moeda(res)


def metade(n = 0, formato=False):
    res = n/2
    return res if not formato else moeda(res)


def moeda(n = 0, moeds = "R$"):
    return f"{moeds}{n:.2f}".replace(".", ",")
    # .replace() substitui oq eu desejar pelo oq eu desejar


def resumo(n, amais, reducao):
    print("-"*30)
    print("RESUMO DO VALOR".center(30)) # .center(deixa centralizado pelo tanto de caracter definido pelo usuário)
    print("-"*30)
    print(f"Preço analisado: \t{moeda(n)}\n"
        f"Dobro do preço: \t{dobro(n, True)}\n"
        f"Metade do preço: \t{metade(n, True)}\n"
        f"{amais}% de aumento: \t{aumentar(n,amais, True)}\n"
        f"{reducao}% de redução: \t{diminuir(n, reducao, True)}")
    print("-"*30) # \t é uma tabulação, o que significa que haverá um espaço parecido com o Tab

