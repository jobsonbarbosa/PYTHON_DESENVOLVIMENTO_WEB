# # Informações do filme
# name = input("Digite o nome do filme:\n")
# yearRelease = int(input("Ano de Lançamento:\n"))
# rating = float(input("Digite a nota de avaliação do filme:\n"))

# # Verifica se o filme é recomentadado
# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} é recomendado.")
# else:
#     print(f"O filme não é recomendado")    

num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))

operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por Zero")
        result = 0

else:
    print("Operação inválida")
    result = 0
    
print(f"O Resultado da operação é: {result:.2f}")