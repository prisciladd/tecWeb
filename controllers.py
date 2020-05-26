# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Post
#from models import Presenca (após criar no models.py)   

@app.route('/post/gravar', methods=['POST']) #recebe mensagem do formulario

def gravar_post():
    
    titulo = request.form['titulo']
    autor = request.form['autor']
    texto = request.form['texto']
    post= Post (titulo, autor, texto)
    post.gravar()
    return redirect('/')


@app.route('/')
def index():
    posts = Post.recupera_todos()
    ## Usamos o objeto retornado por bd() para realizar comandos sql
    
    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'posts': posts
            }
    return render_template('index.html', **context)

@app.route('/post')
def post():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': True,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presencan',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Escrever post', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('post.html', **context)

@app.route('/priscila')
def priscila():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': True,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Sobre - Priscila', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('priscila.html', **context)

@app.route('/anderson')
def anderson():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': True,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Sobre - Priscila', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('anderson.html', **context)

@app.route('/bruno')
def bruno():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': True,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Sobre - Bruno', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('bruno.html', **context)

@app.route('/mateus')
def mateus():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': True,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Sobre - Mateus', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('mateus.html', **context)

@app.route('/gledson')
def gledson():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': True,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Sobre - Gledson', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('gledson.html', **context)

@app.route('/presenca')
def presenca():
    menu = []
    
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': False,
                'href': '/priscila',
                'texto': 'Sobre - Priscila'})
    menu.append({'active': False,
                'href': '/anderson',
                'texto': 'Sobre - Anderson'})
    menu.append({'active': False,
                'href': '/bruno',
                'texto': 'Sobre - Bruno'})
    menu.append({'active': False,
                'href': '/mateus',
                'texto': 'Sobre - Mateus'})
    menu.append({'active': False,
                'href': '/gledson',
                'texto': 'Sobre - Gledson'})
    menu.append({'active': True,
                'href': '/presenca',
                'texto': 'Formulário - Presença'})
    
    context = {'titulo': 'Formulário - Presença', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('presenca.html', **context)

app.run()
