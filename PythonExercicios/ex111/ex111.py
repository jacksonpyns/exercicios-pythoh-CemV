print("Crie um pacote chamado \033[1;31mutilidadesCeV\033[m que tenha dois módulos internos\n"
      "chamados moeda e dado.\n"
      "Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote\n"
      "e mantenha tudo funcionando.")

from utilidadescev import moeda

p = float(input("Preço: R$"))
moeda.resumo(p, 20, 12)
