from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

@app.route('/')
def init():
    return "Hola des de Flask!"

@app.route("/hola/<nom>")
def hola(nom):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # per defecte és en català
    missatge = f"Hola {nom}. La data i hora d'ara mateix és: {formatted_now}"
    
    # paràmetre a la url: http://127.0.0.1:5000/hola/alfonso?lang=en
    idioma = request.args.get('lang')
    if idioma:
        if idioma == "es":
            missatge = f"Hola {nom}. La fecha y hora actual es: {formatted_now}"
        elif idioma == "en":
            missatge = f"Hello {nom}. The current date and time is: {formatted_now}"

    return missatge
