from flask import Flask, render_template, request
import urllib3
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

db = SQLAlchemy(app)

produtos = []
produtos_valores = []

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch

@app.route('/', methods=["GET", "POST"])
def home():
    # produtos = ["Asfalto", "Emulsões", "Aditivos", "CAP", "Lama Asfáltica", "Pintura de Ligação"]
    
    if request.method == "POST":
        if request.form.get("produtos"):
            if request.form.get("produtos") != "Jobson":
                produtos.append(request.form.get("produtos"))
            else:
                produtos.append("Produto proibido")      
        
    return render_template("index.html", produtos=produtos)
  
@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # produtos = {
    #     "Asfalto": 468.49,
    #     "Emulsões": 1523.50,
    #     "Aditivos": 856.90,
    #     "CAP": 3456.10, 
    #     "Asfalto Morno": 4560.00
    # }
    
    if request.method == "POST":
        if request.form.get("produto") and request.form.get("valor"):
            produtos_valores.append({"produto":request.form.get("produto"), 
                                     "valor":request.form.get("valor")})
    return render_template("sobre.html", produtos_valores=produtos_valores)

@app.route('/teste', methods=["GET", "POST"])
def teste():    
    if request.method == "POST":
        if request.form.get("produto") and request.form.get("valor"):
            produtos_valores.append({"produto":request.form.get("produto"), 
                                     "valor":request.form.get("valor")})
    return render_template("teste.html", produtos_valores=produtos_valores)

@app.route("/filmes")
def filmes():
    http = urllib3.PoolManager()

    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=c0accd21d69228a68f7691fa110813e7"

    resposta = http.request('GET', url)

    dados = resposta.data.decode('utf-8')

    jsondados = json.loads(dados)

    return render_template("filmes.html", filmes=jsondados['results'])
  #  return jsondados['results']

#---------------- BANCO DE DADOS ------------------

@app.route("/cursos")
def lista_cursos():
    return render_template("cursos.html", cursos=cursos.query.all())


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)