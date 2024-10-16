from flask import Flask, render_template, request

app = Flask(__name__)

produtos = []
produtos_valores = []

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
    
    if request.method== "POST":
        if request.form.get("produto") and request.form.get("valor"):
            produtos_valores.append({"produto":request.form.get("produto"), "valor":request.form.get("valor")})
    return render_template("sobre.html", produtos_valores=produtos_valores)
app.run(debug=True)