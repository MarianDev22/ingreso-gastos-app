from flask import Flask

app = Flask(__name__)

from app_registro.routes import * #hago referencia a todas las rutas definidas en routes.py

