# 1- Função para imprimir um nome completo
def full_name(firs_name, last_name):
    print(f"Nome é: {firs_name} {last_name}")

full_name("Jobons", "Barbosa")
full_name("Jomeson", "Silva")

# 2 - Função para somar dois numeros
def sum_numbers(a, b):
    return(a + b)
print(f"Soma é: {sum_numbers(5, 20)}")


# 3 - Função com parâmetros default
def address(country="Brasil"):
    print(f"Eu moro em: {country}")
address("Portugal")

# 4 - Função para avaliar filme
def rate_movie(num_rating, movie_name):
    total = 0
    for i in range(num_rating):
        note = float(input("Digite a nota para o filme:\n"))
        total += note
    
    if num_rating > 0:
        average = total / num_rating
    else:
        average = 0
    print(f"Média de avaliação do filme: {movie_name} é: {average:.2f}")

rate_movie(2, "Matrix")
