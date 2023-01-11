from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import date, datetime
from config import *
import os # permite hacer acciones propias del sist op: borrar carpetas, crearlas, etc.

@app.route("/")
def index():
    fichero =open (MOVIMIENTOS_FILE,"r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #prueba de diccionario a vista de html
    datos = [ ]
    for item in csvReader:
        datos.append(item)
    
    fichero.close()
        
    return render_template("index.html", pageTitle="Listas", lista=datos)

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "GET": #esto peuede ser GET o POST
        return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar", pageForm="/new",dataForm={})
    else:
        error =validateForm(request.form)
        
        if error:
            return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar",msjerror=error, dataForm=request.form, pageForm="/new")
        else:
            mifichero = open(MOVIMIENTOS_FILE,"a",newline='')
            lectura =csv.writer(mifichero, delimiter=',',quotechar='"')
            #crear id
            fichero =open (LAST_ID_FILE,"r")
                        
            registro = fichero.read()
            if registro =="":
                new_id = 1
            else:
                new_id= int(registro)+1

            fichero.close()

            ficheroG = open(LAST_ID_FILE,"w")
            ficheroG.write(str(new_id))
            ficheroG.close()
            
            lectura.writerow([new_id,request.form['date'],request.form['concept'],request.form['quantity']])

        mifichero.close()
    return redirect('/')
    

@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        mifichero = open(MOVIMIENTOS_FILE,"r")
        lectura =csv.reader(mifichero, delimiter=',',quotechar='"')
        registro_buscado=[]
        for registro in lectura:
            if registro[0]== str(id):
                registro_buscado= registro
        mifichero.close()

        if len(registro_buscado)>0:
            return render_template("delete.html", pageTitle="Borrar", registros=registro_buscado,typeButton="Borrar")
        else:
            return ("/")
    else:
        fichero_old = open(MOVIMIENTOS_FILE,"r")
        fichero = open(MOVIMIENTOS_NEW_FILE,"w", newline="")
        csvReader= csv.reader(fichero_old, delimiter=',',quotechar='"')
        csvWriter= csv.writer(fichero, delimiter=',',quotechar='"')
        
        for registro in csvReader:
            if registro[0]!= str(id):
                csvWriter.writerow(registro)
        fichero.close()
        fichero_old.close()
        os.remove(MOVIMIENTOS_FILE)
        os.rename(MOVIMIENTOS_NEW_FILE, MOVIMIENTOS_FILE)

        return redirect("/")

@app.route("/update/<int:id>")
def edit(id):
    if request.method == "GET":
        mifichero = open(MOVIMIENTOS_FILE,"r")
        lectura =csv.reader(mifichero, delimiter=',',quotechar='"')
        registro_buscado=[]
        for registro in lectura:
            if registro[0]== str(id):
                registro_buscado= registro
        mifichero.close()
    return render_template("update.html", pageTitle="Editar", typeAction="Actualización",typeButton="Editar", pageForm="/update", registros=registro_buscado)
    #return f"Se va a modificar el id {id}"

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
