frase='   Curso em Vídeo Python   '
print(frase[::2])

print("""We're going to learn operations with strings in Python in this class. 
The main operations that we're going to see are 
Slicing, len() analysis, count(), find(), transformation using replace(), 
upper(), lower(), capitalize(), title(), strip(), merging with join().""")

print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.strip().replace('Python', 'Android'))
