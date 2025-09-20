from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>📋 Control de Asistencia</h1><p>Bienvenido al sistema</p>"

if __name__ == "__main__":
    app.run(debug=True)
