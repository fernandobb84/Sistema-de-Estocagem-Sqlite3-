import sqlite3 as sql

class Banco_de_dados():
    def __init__(self, nome_do_banco='db/banco_de_dados.db'):
        self.conexao = sql.connect(nome_do_banco)
        self.cursor = self.conexao.cursor()

    def salvar(self):
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()


