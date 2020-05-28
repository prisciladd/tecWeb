from banco import bd

class Presente:
    def __init__(self, presenca,pergunta, email, texto):
        self.presenca= presenca
        self.pergunta= pergunta
        self.email= email
        self.texto= texto

    def gravar (self):
        sql = '''insert into presente (presenca, pergunta, email, texto) values (?, ?, ?, ?)'''
        primeiro_interrogacao= self.presenca
        segundo_interrogacao= self.pergunta
        terceiro_interrogacao= self.email
        quarta_interrogacao= self.texto

        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao, quarta_interrogacao])

        bd().commit()
        
    @staticmethod
    def recupera_todos():
        sql = '''select presenca, pergunta, email, texto from presente order by id desc'''
        cur= bd().execute(sql)
        ## Montamos dicionários com os resultados da consulta para passar para a view
        informações = []
        for presenca, pergunta, email, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            dados = Presente(presenca,pergunta, email, texto)
            informações.append(dados)

        return informações 


    

