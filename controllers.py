# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Post


@app.route('/')
def index():
    # mensagens = Mensagem.recupera_todas()
    posts = Post.recupera_todos()

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
                'href': '/fabio',
                'texto': 'Sobre - Fabio'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'posts': posts}

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
                'href': '/fabio',
                'texto': 'Sobre - Fabio'})

    context = {'titulo': 'Escrever post',
            'menu': menu}

    return render_template('post.html', **context)


@app.route('/post/gravar', methods=['POST'])
def gravar_post():
    titulo = request.form['titulo']
    autor = request.form['autor']
    texto = request.form['texto']
    post = Post(titulo, autor, texto)
    post.gravar()
    return redirect('/')

@app.route('/fabio')
def fabio():
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/post',
                'texto': 'Escrever post'})
    menu.append({'active': True,
                'href': '/fabio',
                'texto': 'Sobre - Fabio'})

    context = {'titulo': 'Sobre - Fabio',
            'menu': menu}

    return render_template('fabio.html', **context)


app.run()
