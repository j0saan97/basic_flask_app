import os
import time
import random
import flask_bcrypt
from flask_cors import CORS
from flask import json, jsonify, request, url_for, redirect, session, make_response, send_from_directory
from flask import abort, render_template, render_template_string, Flask, flash
from flask_restful import Resource, Api
import socket
import uuid, datetime
import traceback

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 50
app.config['UPLOAD_PATH'] = 'uploads'
app.config['TEMPLATES_AUTO_RELOAD'] = True

secret = os.urandom(32)
app.config['SECRET_KEY'] = secret
app.secret_key = secret

bcrypt = flask_bcrypt.Bcrypt(app)
CORS(app)
api = Api(app)
PORT_FLASK = 5000

#-------------------------------------------------

@app.route('/actual', methods = ['GET'])
def pagina_actual():
    """
    Mostrar pagina principal
    """
    return render_template('actual.html')

@app.route('/', methods = ['GET'])
def main_page():
    """
    Mostrar pagina principal
    """
    productos = [
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/criticalmax.png', 'texto':'Critical Max', 'precio':125.36},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/dominatrix.png', 'texto':'dominatrix', 'precio':200.0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/greatbud.png', 'texto':'Great Bud', 'precio':250.0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/lemonesia.png', 'texto':'Lemonesia', 'precio':0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/maracuya-diesel.png', 'texto':'Maracuyá Diesel', 'precio':0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/lemon-og.png', 'texto':'Lemon Og', 'precio':0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/og-13.png', 'texto':'OG 13', 'precio':0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/melon-candy.png', 'texto':'Melon Candy', 'precio':0},
                    {'url':'http://192.168.1.131:5000/static/img/ofertas/critical-wido.png', 'texto':'Critical Wido', 'precio':0}
                 ]
    return render_template('main_page.html', productos=productos)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=PORT_FLASK, host='0.0.0.0')
