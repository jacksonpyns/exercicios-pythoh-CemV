# O set é como se fosse uma lista que nao aceita a repetição de elementos
conjunto = set()
# Adicionando um elemento:
conjunto.add("Franjinha")
# removendo elementos que estão dentro de outro set (difference.uppdate)
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}

print(f"O primeiro set contém {conjunto1}")
print(f"O primeiro set contém {conjunto2}")
conjunto1.difference_update(conjunto2)
print(f"O primeiro set contém {conjunto1}")

# remover um elemento especifico do set (remove)
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto1.remove("Mega Drive")
print(conjunto1)

# remover um elemento especifico do set (discard)
conjunto1.discard("Super Nintendo")
print(conjunto1)
conjunto1.discard("Super Nintendo") # SE EU TENTAR REMOVER NOVAMENTE, COM O discard NÃO OUVERÁ ERRO
