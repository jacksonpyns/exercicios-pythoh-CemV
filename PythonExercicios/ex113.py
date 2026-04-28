print("Reescreva a função \033[1;34mleiaInt()\033[m que fizemos no desafio 104, incluindo agora\n"
      "a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma\n"
      "função \033[1;34mleiaFloat()\033[m com a mesma funcionalidade.")

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print("\n\033[1;33mUsuário preferiu não digitar esse número!\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print("\n\033[1;33mUsuário preferiu não digitar esse número!\033[m")
            return 0
        else:
            return n


i = leiaInt("Digite um Inteiro: ")
f = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {i} e o real foi {f}")

#print('\033[1;31mErro! Digite um número inteiro válido.\033[m')