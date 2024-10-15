movieName = "Game Of Throneses"
movieDescripton = "Game Of Thrones é uma serie mediéval com Dragões"

print(movieName.upper()) # tudo maiúsculo
print(movieName.lower()) # tudo minúsculo

print(movieName.capitalize()) # Primeira Letra maiúscula
print(movieName.title()) # Primeira Letra maiúscula
print(movieName.center(15, '-')) # Retorna string centralizada com caracteres de preenchuimento
print(movieName.find("Of")) #  retorna a posiação de uma determinado caracter
print(movieName.count("e")) #  conta os caracteres
print(movieName.replace("Of", "Dos")) # Substitui elemento por outro
print(movieName.split(' '))