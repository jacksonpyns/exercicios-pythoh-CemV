def aumentar(n = 0):
    return n * 0.1 + n


def diminuir(n = 0):
    return n - (n * 0.1)


def dobro(n = 0):
    return n*2


def metade(n = 0):
    return n/2


def moeda(n = 0, moeds = "R$"):
    return f"{moeds}{n:.2f}".replace(".", ",")
    # .replace() substitui oq eu desejar pelo oq eu desejar


