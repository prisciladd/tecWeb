# cria_bd.py
# Execute esse arquivo para atualizar o banco

from aplicacao import app
from contextlib import closing
from banco import conectar_bd

def criar_bd():
    with closing(conectar_bd()) as bd:
        with app.open_resource('esquema.sql') as sql:
            bd.cursor().executescript(sql.read().decode('utf-8'))
        bd.commit()

criar_bd()
