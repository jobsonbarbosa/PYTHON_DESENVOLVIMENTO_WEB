import pprint

filmsDict = {
    "inception": {
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar": {
    "yearRelease": 2014,
    "imdbRating": 9.3,
    "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight": {
    "title": "Inception",
    "yearRelease": 2008,
    "imdbRating": 9.0,
    "genre": ["Action", "Crime", "Dama"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionario aninhado
print(filmsDict["interstellar"]["genre"])

# 2 - Adicionar novo item
filmsDict["inception"]["director"] = "Christopher Nolan"
print(filmsDict["inception"])

# 3 - Excluir um dicionario
del filmsDict["the dark knight"]
pp.pprint(filmsDict)