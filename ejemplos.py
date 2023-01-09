#lectura de archivos    
with open('data/movimientos.txt',"r") as resultado:
    leer= resultado.read()
    print (leer)

#otra manera
result = open ('data/movimientos.txt',"r")
lectura = result.readlines()
print(lectura)
import csv

datos = []
mifichero= open ('data/movimientos.txt',"r")
mifichero = csv.reader(mifichero, delimiter=",",quotechar='"')

for registros in mifichero:
    print(registros)
    datos.append(registros)