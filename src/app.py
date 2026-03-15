from flask import Flask

app = Flask(__name__)


@app.route("/status")
def status():
    return {"status:" "API online"}

@app.route("/")
def home():
    return "Sistema de Biblioteca Online"

@app.route("/")
def home():
    return "Sistema de Gestão de Biblioteca"
@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"







if __name__ == "__main__":
    app.run(debug=True)