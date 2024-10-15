# contatena

name = input("Digite o nome do filme:\n")
yearLaunche = int(input("Digite o ano de lancemanto:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

# Alternativa 1
print("Dados do Filme")
print("=====================================")

# print("Nome do filme: ", name)
# print("Ano de lançamneto: ", yearLaunche)
# print("Nota do filme: ", noteMovie)

# Alternatica 2
# print("Nome do Filme: ", name, "\nAno de Lançamento", yearLaunche, "\nNota do Filme: ", noteMovie)

# Alternatica 3 - usando F string
print(f"Nome do Filme: {name}")
print(f"Ano de Lançamento: {yearLaunche}")
print(f"Nota do Filme: {noteMovie}")