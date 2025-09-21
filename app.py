from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>📋 Control de Asistencia</h1><p>Bienvenido al sistema</p>"

@app.route("/recibir_evento", methods=["POST"])
def recibir_evento():
    data = request.data.decode("utf-8")
    print("Evento recibido:", data)
    return "OK", 200