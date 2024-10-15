# - Dicionario, muito parecido com o JSON, usando chave valor

filmsInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}
print(filmsInception)
print(len(filmsInception))
print(type(filmsInception))


# 1 - Recuperar um elemento do dicionario
print(filmsInception["genre"])
print(filmsInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(filmsInception.keys())

# 3 - Buscar apenas os valores do dicioario
print(filmsInception.values())

# 4 - Buscar itens do dicionario com chave e valor
print(filmsInception.items())

# 5 - Adicionar itens no dicionario
filmsInception["director"] = "Christopher Nolan"
print(filmsInception)

# 6 - Atualizar itens no dicionario
filmsInception.update({"imdbRating": 9.1})
print(filmsInception)

# 7 - Remover item do dicionario
filmsInception.pop("director")
print(filmsInception)
