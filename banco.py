# banco.py

import sqlite3
from flask import g
from aplicacao import app

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def pre_requisicao():
    g.db = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.db.close()

def bd():
    return g.db
