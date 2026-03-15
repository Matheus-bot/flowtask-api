from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "API funcionando corretamente"}
@app.route("/status")
def status():
    return {"status:" "API online"}

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Biblioteca"


if __name__ == "__main__":
    app.run(debug=True)