from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import date, datetime
from config import *
import os

def select_all():
    fichero =open (MOVIMIENTOS_FILE,"r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    datos = [ ]
    for item in csvReader:
        datos.append(item)
    
    fichero.close()

    return datos

def select_by(id):
    mifichero = open(MOVIMIENTOS_FILE,"r")
    lectura =csv.reader(mifichero, delimiter=',',quotechar='"')
    registro_buscado=[]
    for registro in lectura:
        if registro[0]== str(id):
            registro_buscado= registro
    
    diccionario = dict()
    
    diccionario["id"]= registro_buscado [0]
    diccionario["date"]= registro_buscado[1]
    diccionario["concept"]= registro_buscado[2]
    diccionario["quantity"]= registro_buscado [3]

    mifichero.close()
    return diccionario

def delete_by(id):
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

def insert(registro_form):
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
    
    lectura.writerow([str(new_id)]+registro_form)

    mifichero.close()

def update_by(id):
    fichero_old = open(MOVIMIENTOS_FILE,"r")
    fichero = open(MOVIMIENTOS_NEW_FILE,"w", newline="")
    csvReader= csv.reader(fichero_old, delimiter=',',quotechar='"')
    csvWriter= csv.writer(fichero, delimiter=',',quotechar='"')
    
    for registro in csvReader:
        if registro[0]!= str(id):
            csvWriter.writerow(registro)
    fichero.close()
    fichero_old.close()