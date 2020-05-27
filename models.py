## models.py
from banco import bd


class Post:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo
        self.autor = autor
        self.texto = texto

    def gravar(self):
        sql = '''insert into posts (titulo, autor, texto) values (?, ?, ?)'''
        primeiro_interrogacao = self.titulo
        segundo_interrogacao = self.autor
        terceiro_interrogacao = self.texto
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao])
        bd().commit()

    @staticmethod
    def recupera_todos():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''select titulo, autor, texto from posts order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        posts = []
        for titulo, autor, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            post = Post(titulo, autor, texto)
            posts.append(post)
        
        return posts
