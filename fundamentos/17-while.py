# Lista de Filmes
movieFilms = ["Marverick", "Interestelar", "Inception", "Jurassic Park"]

# 1- Iterando valores de uma Lista de Filmes usando while
index = 0

while(index < len(movieFilms)):
    print(movieFilms[index])
    index += 1
    
# 2 - Quando a condição for atendida, o loop será encerrado
index = 0

while(index < len(movieFilms)):
    if(movieFilms[index] == "Inception"):
        break
    print(movieFilms[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
index = 0

while(index < len(movieFilms)):
    if(movieFilms[index] == "Inception"):
        index += 1
        continue
    print(movieFilms[index])
    index += 1
    
# 4 - Avaliação do filme usando o While
movieName = input("Digite o nome do Filme:\n")
movieRating = int(input("Digite quantas avaliaçãoes deseja fazer:\n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    avarage = total / movieRating
else:
    avarage = 0

print(f"Média da avaliação do filme {movieName} é: {avarage:.2f}")