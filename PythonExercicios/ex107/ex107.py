print("Crie um módulo chamado \033[1;31mmoeda.py\033[m que tenha as funções incorporadas \033[1;34m\n"
      "aumentar(), diminuir(), dobro() e metade()\033[m.")
print("Faça também um programa que importe esse módulo e use algumas dessas funções.")

import moeda

num = float(input("Digite o preço: R$"))
print(f"A metade de R${num:.2f} é R${moeda.metade(num):.2f}")
print(f"O dobro de R${num:.2f} é R${moeda.dobro(num):.2f}")
print(f"Aumentando 10%, temos R${moeda.aumentar(num):.2f}")
print(f"Diminuindo 10%, temos R${moeda.diminuir(num):.2f}")