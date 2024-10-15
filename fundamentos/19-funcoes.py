# para criar uma função usa-se a palavra reservada def

# 1 - Função para imprimir uma mensagem
def imprimir():
    print("Sistema e Filmes")

# for i in range(10):
#     imprimir()

# 2 - Calcular media de notas
def calculete_average():
    num_average = int(input("Digite quantas avaliações deseja fazer para o flme:\n"))
    total = 0
    for i in range(num_average):
        note = float(input("Digite a nota do filme:\n"))
        total += note
    if num_average > 0:
        average = total / num_average
    else:
        average = 0
    
    return average

print(f"A média de avaliações é: {calculete_average():.2f}")

# 3 - Função para cadastrar um filme

def create_movie():
    name = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input("Digita a nota do filme:\n"))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice}:.2f")

create_movie()