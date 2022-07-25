from connect_db import Database


class Usuarios(object):
    def __init__(self, id_usuario=0, nome='', cpf='', email='', telefone='', senha=''):
        self.info = {}
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

    # A classe usuários deve permitir as operações de select, update, insert e delete

    def selectUsuario(self, v_idusuario):
        # 1 - estabelecer a conexão com o banco
        database = Database()

        try:
            # criar um cursor para suportar a execução de comandos SQL
            cursor = database.conexao.cursor()

            # OBSERVAÇÕES
            # 1- Executar o comanndo SQL com variáveis!
            cursor.execute("""select 
                                * 
                            from 
                                usuarios 
                            where 
                                id_usuario = ?;""",
                           (v_idusuario,))

            # 2- Mostrar o resultado do comando SELECT
            print("ID, nome, cpf, email, telefone e senha")
            for linha in cursor.fetchall():
                print(linha)

            # Fechar a conexao com o banco
            cursor.close()

            return "Operação realizada com sucesso!"
        except:
            "Ocorreu um erro ao pesquisar no database!"

    # implementar o SQL INSERT
    def insertUsuario(self, nome, cpf, email, telefone, senha):

        database = Database()

        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

        try:
            cursor = database.conexao.cursor()
            cursor.execute("""insert into 
                                usuarios (nome, cpf, email, telefone, senha) 
                                values (?, ?, ?, ?, ?);""",
                           (self.nome, self.cpf, self.email, self.telefone, self.senha))

            database.conexao.commit()
            cursor.close()

            print("Usuário inserido com sucesso!")

        except:
            return "Ocorreu um erro ao pesquisar no database!"

    # implementar o SQL UPDATE
    def updateUsuario(self, nome, cpf, email, telefone, senha, v_idusuario):

        database = Database()

        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

        try:
            cursor = database.conexao.cursor()

            cursor.execute("""update 
                                usuarios
                            set 
                                nome = ?, 
                                cpf = ?, 
                                email = ?, 
                                telefone = ?,
                                senha = ? 
                            where 
                                id_usuario = ?;""",
                           (self.nome, self.cpf, self.email, self.telefone, self.senha, v_idusuario))

            database.conexao.commit()
            cursor.close()

            print("Usuário atualizado com sucesso!")

        except:
            "Ocorreu um erro ao pesquisar no database!"

    # implementar o SQL DELETE
    def deleteUsuario(self, v_idusuario):

        database = Database()

        try:
            cursor = database.conexao.cursor()

            cursor.execute("""delete from 
                                usuarios 
                            where 
                                id_usuario = ?""",
                           (v_idusuario,))
            database.conexao.commit()

            cursor.close()

            return "Operação realizada com sucesso!"
        except:
            "Ocorreu um erro ao pesquisar no database!"
