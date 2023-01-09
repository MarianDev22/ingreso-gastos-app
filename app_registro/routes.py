from app_registro import app
from flask import render_template

@app.route("/")
def index():
    #prueba de diccionario a vista de html
    datos = [
        {
            'fecha':'18/12/22',
            'concepto': 'Regalo de Reyes',
            'cantidad':-275.50
        },
        {
            'fecha':'19/12/22',
            'concepto':'Cobro de trabajo',
            'cantidad':1200
        },
        {
            'fecha':'18/12/22',
            'concepto':'Ropa de Navidad',
            'cantidad':-355.50
        }
    ]
    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new")
def create():
    return render_template("new.html", pageTitle="Alta")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Borrar")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Editar")