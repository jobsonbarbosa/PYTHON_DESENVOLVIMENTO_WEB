# - O set usa {}
filmsSet = { "Inception", "Redemption", "Matrix", "Dark", "Albatroz", "Interstellar" }

print(type(filmsSet))

# 1 - Buscar o tamanho do Set
print(len(filmsSet))

# 2 - True e 1 são considerados o mesmo valor

exampleSet = {"Matrix", True, 1, 8.4, "Abacate"}
print(exampleSet)

# 3 - Adicionar item de outro set
filmsSet.update(exampleSet)
print(filmsSet)

# - Remover um item do set
filmsSet.remove(True)
filmsSet.remove(8.4)
print(filmsSet)