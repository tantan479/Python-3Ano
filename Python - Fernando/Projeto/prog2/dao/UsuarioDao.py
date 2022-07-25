from model.Usuario import Usuario


class UsuarioDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarUsuarios(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM usuario'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            usuario = Usuario()
            usuario.id = item[0]
            usuario.nome = item[1]
            usuario.email = item[2]
            usuario.senha = item[3]

            lista.append(usuario)

        return lista

    def 
