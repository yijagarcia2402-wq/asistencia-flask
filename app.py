from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>📋 Control de Asistencia</h1><p>Bienvenido al sistema</p>"

# 🔹 Nuevo endpoint para recibir eventos del Hikvision
@app.route("/recibir_evento", methods=["POST"])
def recibir_evento():
    data = request.data.decode("utf-8")  # el Hikvision manda XML en texto
    print("Evento recibido:", data)       # esto quedará en los logs de Render
    return "OK", 200