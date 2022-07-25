from config.Config import Config
from config.Database import Database
from model.Usuario import Usuario
from dao.UsuarioDao import UsuarioDao
from view.Table import Table

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)
lista = dao.selecionarUsuarios()
tela = Table(lista)


