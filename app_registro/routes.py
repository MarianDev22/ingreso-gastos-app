from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import date, datetime

@app.route("/")
def index():
    fichero =open ("data/movimientos.csv","r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #prueba de diccionario a vista de html
    datos = [ ]
    for item in csvReader:
        datos.append(item)
        
    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "GET": #esto peuede ser GET o POST
        return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar", pageForm="/new",dataForm={})
    else:
        mifichero = open("data/movimientos.csv","a",newline='')
        lectura =csv.writer(mifichero, delimiter=',',quotechar='"')

        error =validateForm(request.form)
        
        if error:
            return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar",msjerror=error, dataForm=request.form, pageForm="/new")
        else:
            lectura.writerow([request.form['date'],request.form['concept'],request.form['quantity']])

        mifichero.close()
    return redirect('/')
    

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Borrar")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Editar", typeAction="Actualización",typeButton="Editar", pageForm="/update")


def validateForm(requestForm):
    hoy = date.today().isoformat()
    errores=[]
    if requestForm['date'] > hoy:
            errores.append("Fecha inválida: La fecha introducida es a futuro")
    if requestForm['concept'] =="":
        errores.append("Concepto vacío: Escriba un concepto")        
    if requestForm['quantity'] =="" or float(requestForm['quantity']) == 0:
        errores.append("Cantidad vacía o cero: debe ingresar un número mayor o menor a cero")
    return errores
