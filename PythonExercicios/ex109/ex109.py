print("Modifique as funções que foram criados no desafio 107 para que elas aceitem um parâmetro\n"
      "a mais, informando se o valor retornado por elas vai ser ou não formatado pela função\n"
      "moeda(), desenvolvida no desafio 108.")

import moeda

num = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(num, 10, True)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(num, 10, True)}")
print(f"Aumentando 13%, temos {moeda.aumentar(num, 13, True)}")