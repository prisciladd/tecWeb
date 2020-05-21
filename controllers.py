# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Post

@app.route('/post/gravar', methods=['POST']) #recebe mensagem do formulario

def gravar_post():
    #mensagens= Mensagem (request.form['usuario'],
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
    
    context = {'titulo': 'Escrever post', #muda frase na tela e tiitulo página
            'menu': menu}
    return render_template('post.html', **context)
app.run()
