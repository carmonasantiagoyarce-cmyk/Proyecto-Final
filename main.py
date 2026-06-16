from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
from speak_module import *


model = tf.keras.models.load_model("model/keras_model.h5")
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/final", methods=["POST"])
def final():
    nombre = request.form["nombre"]
    archivo = request.files["archivo"]

    ruta = "uploads/" + archivo.filename
    archivo.save(ruta)

    try:
        img = Image.open(ruta).convert("RGB")
        img = img.resize((224, 224))
    except:
        return render_template("error.html",filename=archivo.filename)

    # IA 👇
    img = Image.open(ruta).resize((224, 224))
    img_array = np.array(img, dtype=np.float32)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediccion = model.predict(img_array)

    clases = ["Carton", "Metal","Organico","Papel","Plastico","Vidrio","No aprobechable"]
    resultado = clases[np.argmax(prediccion)]
    tipo = resultado.lower()
    nombre_simplificado = "ninguna"

    if tipo == "papel":
        caneca = "⚪ Caneca Blanca (Reciclables)"
        nombre_simplificado = "blanca"

    elif tipo == "plastico" or tipo == "metal" or tipo == "vidrio":
        caneca = "⚪ Caneca Blanca (Reciclables)"
        nombre_simplificado = "blanca"

    elif tipo == "organico":
        caneca = "🟢 Caneca Verde (Orgánicos)"
        nombre_simplificado = "verde"

    else:
        caneca = "⚫ Caneca Negra (No aprovechables)"
        nombre_simplificado = "negra"
    return render_template(
    "result.html",
    nombre=nombre,
    resultado=resultado,
    caneca=caneca,
    classed=nombre_simplificado,
)

@app.route("/final_q",methods=["POST"])
def final_quest():
    if request.form.get("inicio"):
        return render_template("index.html")
    if request.form.get("guia"):
        return render_template("guia.html")
    if request.form.get("quest"):
        return render_template("quest.html")
@app.route("/quiz", methods=["POST"])
def quiz():

    puntaje = 0

    if request.form.get("p1") == "blanca":
        puntaje += 1

    if request.form.get("p2") == "verde":
        puntaje += 1

    if request.form.get("p3") == "carton":
        puntaje += 1

    if request.form.get("p4") == "verde":
        puntaje += 1

    if request.form.get("p5") == "servilleta":
        puntaje += 1

    if request.form.get("p6") == "reciclar":
        puntaje += 1

    if request.form.get("p7") == "blanca":
        puntaje += 1

    if request.form.get("p8") == "hojas":
        puntaje += 1

    if request.form.get("p9") == "blanca":
        puntaje += 1

    if request.form.get("p10") == "no_aprovechables":
        puntaje += 1

    return render_template(
        "resultado_quiz.html",
        puntaje=puntaje
    )
if __name__ == "__main__":
    hablar("Bienvenido a  EcoGuardian, un clasificador de residuos con IA")
    app.run(debug=True)