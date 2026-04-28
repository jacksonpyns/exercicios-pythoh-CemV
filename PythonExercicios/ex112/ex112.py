print("Dentro do pacote \033[1;31mutilidadeCeV\033[m que criamos no desafio 111, temos um módulo\n"
      "chamado dado. Crie uma função chamada \033[1;34mleiaDinherio()\033[m que seja capaz de funcionar\n"
      "como a função \033[1;34minput()\033[m, mas com uma validação de dados para aceitar apenas valores\n"
      "que sejam monetários.")

from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(p, 35, 22)
