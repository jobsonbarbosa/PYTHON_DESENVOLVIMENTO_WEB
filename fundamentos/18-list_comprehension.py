# 1 - Listando valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de Filmes
movieList = ["Marverick", "Interestelar", "Inception", "Jurassic Park", "Park Jobs", "Titaball", "Titanic"]

# 2 - Filmes que possuiem a letra e no titulo
movieWithe= [movie for movie in movieList if 'u' in movie.lower()]
print(movieWithe)

# 3 - Filmes que assistir

movieWatched = [movie for movie in movieList if movie != "Inception"]
print(movieWatched)

# 4 - Encontrando um filme pelo nome

movieName = [movie for movie in movieList if movie == "Interestelar"]
print(movieName)

while True:
    seachName = input("Digite o nome do filme para buscar da lista (ou sair para encerrar):\n")
    if seachName.lower() == "sair":
        print("Programa Encerrado")
        break
    foundMovies = [movie for movie in movieList if seachName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {seachName}:")
        for foundMovie in foundMovies:
            print(foundMovie)
        else:
            print(f"Nenhum filme foi encontrado com o noe {seachName}. Tente novamente.")