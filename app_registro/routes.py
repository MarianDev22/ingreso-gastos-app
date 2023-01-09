from app_registro import app
from flask import render_template
import csv

@app.route("/")
def index():
    fichero =open ("data/movimientos.txt","r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #prueba de diccionario a vista de html
    datos = [ ]
    for item in csvReader:
        datos.append(item)
        '''
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
    '''
    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new", method=["get","post"])
def create():
    return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Borrar")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Editar", typeAction="Actualización",typeButton="Editar")