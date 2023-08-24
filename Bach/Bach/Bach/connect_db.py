# Importando o módulo do SQLite

import sqlite3


class Database:
    def __init__(self):
        self.conexao = sqlite3.connect('banco_app.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists usuarios(
                        id_usuario integer primary key autoincrement,
                        nome text,
                        cpf text,
                        email text,
                        telefone text,
                        senha text)""")
        self.conexao.commit()
        c.close()
