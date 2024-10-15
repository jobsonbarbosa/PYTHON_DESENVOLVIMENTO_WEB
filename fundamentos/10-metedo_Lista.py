filmsList = ["Inception", "Redemption", "Matrix", "Dark", "Albatroz"]
print(filmsList)

# 1- Tamanho da lista

print(len(filmsList)) 

# 2 - Recuperar item da lista pelo  indice
print(filmsList.index("Matrix"))

# 3 - Adicionar item ao final da lista
print(filmsList.append("Jogos Vorazes"))
print(filmsList)
print(len(filmsList))

# 4 - Ordenação da lista
filmsList.sort()
print(filmsList)

# 5 - Copia os idem de uma lista para o outro
filmsCopy = filmsList.copy()
filmsCopy.remove("Albatroz")
print(filmsCopy)
print(filmsList)

# 6 - Remoce todos os itens da lista

filmsList.clear()
print(filmsList)