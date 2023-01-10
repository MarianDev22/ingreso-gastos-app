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
        error =validateForm(request.form)
        
        if error:
            return render_template("new.html", pageTitle="Alta", typeAction= "Alta", typeButton="Guardar",msjerror=error, dataForm=request.form, pageForm="/new")
        else:
            mifichero = open("data/movimientos.csv","a",newline='')
            lectura =csv.writer(mifichero, delimiter=',',quotechar='"')
            #crear id
            fichero =open ("data/last_id.csv","r")
                        
            registro = fichero.read()
            if registro =="":
                new_id = 1
            else:
                new_id= int(registro)+1

            fichero.close()

            ficheroG = open("data/last_id.cvs","w")
            ficheroG.write(str(new_id))
            ficheroG.close()
            
            lectura.writerow([new_id,request.form['date'],request.form['concept'],request.form['quantity']])

        mifichero.close()
    return redirect('/')
    

@app.route("/delete/<int:id>")
def remove(id):
    #return render_template("delete.html", pageTitle="Borrar")
    return f"Se va a eliminar el id {id}"

@app.route("/update/<int:id>")
def edit(id):
    #return render_template("update.html", pageTitle="Editar", typeAction="Actualización",typeButton="Editar", pageForm="/update")
    return f"Se va a modificar el id {id}"

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
