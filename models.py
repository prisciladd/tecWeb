from banco import bd

class Mensagem:
    def __init__(self, usuario, texto):
        self.usuario= usuario
        self.texto= texto

    def gravar (self):
        sql = '''insert into mensagens (usuario, texto) values (?, ?)'''

        bd().execute(sql, [self.usuario, self.texto])

        bd().commit()   

    @staticmethod
    def recupera_todas():
        sql = '''select usuario, texto from mensagens order by id desc'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        mensagens = []
        for usuario, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            mensagem=Mensagem (usuario,texto)
            mensagens.append(mensagem)

        return mensagens

