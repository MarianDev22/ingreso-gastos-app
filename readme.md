# Acplicación Web Ingresos Gastos

- Programa hecho en Python con el framework Flask, App Ingresos Gastos 

## Instalación
En su entorno de Python ejecutar el siguiente comando:
```
pip install -r requirements.txt
```

La librería utilizada flask https://flask.palletsprojects.com/en/2.2.x

## Ejecución del programa
- Inicializar el servidor de Flask
    en Mac: 
    ```
    export FLASK_APP=hello.py
    ```
    en Windows:
    ```
    set FLASK_APP=hello.py
    ```
## Comando para ejecutar el servidor:
```
flask --app hello run
```

## Comando para cctualizar el servidor con cambios de codigo en tiempo real
```
flask --app hello --debug run
```

## Comando espcial para lanzar el servidor en un puerto diferente en caso de que esté ocupado:
```
flask --app hello run -p 5001
```

## Comando para lanzar en modo debug y con puerto cambiado
```
flask --app hello --debug run -p 5001
```