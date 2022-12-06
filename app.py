from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin  #Para poder atender las peticiones localmente
from flask import render_template
from flask import abort, jsonify
from persontext import predict_personalidad
from werkzeug.utils import redirect
import os

app = Flask(__name__)

#Para poder atender las peticiones locales
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    """
    Página inicial
    """
    return "<h1>Bienvenidos a ApiPersonText v0.11<h1>"

#@app.route('/anylink')
#def anylink():
#    pass

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/persontext/neuroticismo/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_neuroticismo(texto):
    datos = {}
    prediccion = predict_personalidad(texto.lower(),"neuroticismo")
    datos["presenta_neuroticismo"] = prediccion
    return jsonify(datos)

@app.route('/persontext/responsabilidad/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_responsabilidad(texto):
    datos = {}
    prediccion = predict_personalidad(texto.lower(),"responsabilidad")
    datos["presenta_responsabilidad"] = prediccion
    return jsonify(datos)


if __name__ == "__main__":
   app.run() ##Replaced with below code to run it using waitress 
   #serve(app, host='0.0.0.0', port=5000, url_scheme='https')