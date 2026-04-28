print('Crie um programa onde o usuário digite uma expressão qualquer que use \033[31mparênteses\033[m.\n'
      'Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados\n'
      'na ordem correta.')

expr = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in expr:
      if simb == '(':
            pilha.append('(')
      elif simb == ')':
            if len(pilha) > 0:
                  pilha.pop()
            else:
                  pilha.append(')')
                  break
if len(pilha) == 0:
      print('Sua expressão está válida!')
else:
      print('Sua expressão está inválida!')

