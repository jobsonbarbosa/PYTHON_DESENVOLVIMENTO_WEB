from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    produtos = ["Asfalto", "Emulsões", "Aditivos", "CAP", "Lama Asfáltica", "Pintura de Ligação"]
        
    return render_template("index.html", produtos=produtos)
  
@app.route('/sobre')
def sobre():
    produtos = {
        "Asfalto": 468.49,
        "Emulsões": 1523.50,
        "Aditivos": 856.90,
        "CAP": 3456.10 
    }
    return render_template("sobre.html", produtos=produtos)
app.run(debug=True)