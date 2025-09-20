from flask import Flask, request

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>📋 Control de Asistencia</h1><p>Bienvenido al sistema</p>"

# 🔹 Aquí está el endpoint que espera el Hikvision
@app.route("/recibir_evento", methods=["POST"])
def recibir_evento():
    data = request.data.decode("utf-8")
    print("Evento recibido:", data)
    return "OK", 200