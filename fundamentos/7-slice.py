movieName = "Game Of Thrones"

# string[inicio:fim] - indice começa na posição 0 | indice final -1

# 1 - Buscar toda string a partir da primeira posição

print(movieName[5:])

# 2 - Buscar toda string até a última posiação
print(movieName[:5])

# 3- Busca toda a string da terceira até a ultima posição
print(movieName[2:])

'''
string[inicio:passo] - indice começa na posição 0 | indice final -1
passo - determina o incremento. Por padrão esse número é o 1
'''

# 4- Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5- Buscar toda string nos indices impares
print(movieName[1::2])

# 6 - inverter uma string de trás para frente
print(movieName[::-1])