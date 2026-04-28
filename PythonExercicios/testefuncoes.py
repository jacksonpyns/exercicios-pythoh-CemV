import funcoes

funcoes.alunos_de_fisica()

def somar(a:float, b:float):
    """Função que realiza a soma entre dois valores e retorna o resultado.
    Dois argumentos, 'a' e 'b', são obrigatórios e do tipo float."""
    return a + b

#para acessar o doc """ que está dentro do somar
print(help(somar)) #ou
print(somar.__doc__)
