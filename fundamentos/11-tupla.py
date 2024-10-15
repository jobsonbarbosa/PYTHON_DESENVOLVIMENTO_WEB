# Na tupla usa-se os {}
filmsTuple = ("Inception", "Redemption", "Matrix", "Dark", "Albatroz", "Interstellar")

print(type(filmsTuple))

# 1 - Buscar os dois primeiros indices da Tupla
print(filmsTuple[:2])

# 2 0 Buscar o último item da Tupla
print(filmsTuple[-1])

# 3 - Filmes até uma posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsTuple[1:5])

# 5 - Recuperar um item da tuplo pelo nome
print(filmsTuple.index("Redemption"))