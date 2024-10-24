import urllib3
import json

http = urllib3.PoolManager()

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=c0accd21d69228a68f7691fa110813e7"

resposta = http.request('GET', url)

dados = resposta.data.decode('utf-8')

jsondados = json.loads(dados)

print(jsondados['results'])
# resposta = http.request('GET', url)

# if resposta.status == 200:
#     dados = resposta.data.decode('utf-8')
#     print("Resposta:", dados)
    
#     try:
#         dados_json = json.loads(dados)
#         print("JSON:", dados_json)
#     except json.JSONDecodeError as e:
#         print("Erro ao carregar JSON:", e)
# else:
#     print("Erro", resposta.status)


# dados = resposta.read().decode('utf-8')
# dados_json = json.loads(dados)
# print(dados_json)