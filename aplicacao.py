# aplicacao.py

from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

# configuração
app.config.update(
    DATABASE = 'banco.db',
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default',
)

