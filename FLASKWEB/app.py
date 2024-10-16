from flask import Flask, render_template, request

app = Flask(__name__)

produtos = []

@app.route('/', methods=["GET", "POST"])
def home():
    # produtos = ["Asfalto", "Emulsões", "Aditivos", "CAP", "Lama Asfáltica", "Pintura de Ligação"]
    
    if request.method == "POST":
        if request.form.get("produtos"):
            produtos.append(request.form.get("produtos"))        
        
    return render_template("index.html", produtos=produtos)
  
@app.route('/sobre')
def sobre():
    produtos = {
        "Asfalto": 468.49,
        "Emulsões": 1523.50,
        "Aditivos": 856.90,
        "CAP": 3456.10, 
        "Asfalto Morno": 4560.00
    }
    return render_template("sobre.html", produtos=produtos)
app.run(debug=True)