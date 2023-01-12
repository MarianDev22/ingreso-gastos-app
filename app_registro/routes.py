from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import date, datetime
from config import *
import os # permite hacer acciones propias del sist op: borrar carpetas, crearlas, etc.
from models import *

@app.route("/")
def index():
    datos = select_all()
        
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
            insert([request.form['date'],request.form['concept'],request.form['quantity']])

        
    return redirect('/')
    

@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):
    if request.method == "GET":

        registro_buscado = select_by(id)

        if len(registro_buscado)>0:
            return render_template("delete.html", pageTitle="Borrar", registros=registro_buscado,typeButton="Borrar")
        else:
            return redirect("/")
    else:
        delete_by(id)

        return redirect("/")

@app.route("/update/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "GET":

        registro= select_by(id)
        return render_template("update.html", pageTitle="Modificación", typeAction="Modificación",typeButton="Editar", dataForm=registro, pageForm="/update/"+str(id))
    else:
        error =validateForm(request.form)
        
        if error:
            return render_template("update.html", pageTitle="Modificación", typeAction= "Modificación", typeButton="Editar",msjerror=error, dataForm=request.form)
        else:
            update_by(id,[request.form['date'],request.form['concept'],request.form['quantity']])

            
    return redirect("/")

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
