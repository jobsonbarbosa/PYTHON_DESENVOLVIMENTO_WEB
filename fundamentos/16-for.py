# Lista de Filmes
movieFilms = ["Marverick", "Interestelar", "Inception", "Jurassic Park"]

# 1- Iterando valores de uma Lista
for movie in movieFilms:
    print(movie)

# 2 - Break no laço, quando a condição for atendida o laço será encerrado
for movie in movieFilms:
    if movie == "Inception":
        break
    print(movie)
    
# 3 - Continue, quando a condição for atendida o Loop vai para a proxima iteração
for movie in movieFilms:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Avaliação do Filme
movieName = input("Digite o nome do Filme:\n")
movieRating = int(input("Digite quantas avaliaçãoes deseja fazer:\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"A media de Avaliação do filme {movieName} é: {average:.2f}")