print("Adapte o código do desafio 107, criando uma função adicional chamado moeda() que\n"
      "consiga mostrar os valores como um valor monetário formatado.")

import moeda

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num))}")
print(f"Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(num))}")