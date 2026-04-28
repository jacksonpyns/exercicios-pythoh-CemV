# TRATAMENTO DE ERROS E EXCEÇÕES
try: # try é tente
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

except: # se der erro
    print("Infelizmente tivemos um problema... : ")

else: # se deu certo /opcional
    print(f"O resultador é {r:.1f}")

finally: # vai acontecer independente se deu CERTO ou se deu ERRO /opcional
    print("Volte sempre! Muito obrigado!")

'''
except Exception as erro: # para dizer qual foi o motivo do erro
    print(f"Problema encontrado foi {erro.__class__}")
except (ValueError, TypeError)
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!)
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
    '''

