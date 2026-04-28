print("Adicione ao módulo \033[1;31mmoeda.py\033[m criado nos desafios anteriores, uma função\n"
      "chamada \033[1;34mresumo()\033[m, que mostre na tela algumas informações geradas pelas\n"
      "funções que já temos no módulo criado até aqui.")

import moeda

num = float(input("Digite o preço: R$"))
moeda.resumo(num, 10, 5)