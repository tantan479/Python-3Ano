from user_app import Usuarios
import time
import os


class App:
    def __init__(self):
        pass


def menu():
    op = 0
    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print("\n--------------------MENU--------------------")
        print("1 - Inserir um novo usuário")
        print("2 - Buscar um usuário já existente")
        print("3 - Alterar o registro de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Fechar o programa")
        print("--------------------------------------------\n")
        op = int(input("Digite a opção desejada: "))
    return op


def main():

    opc = 0

    while opc != 5:
        opc = menu()
        usuario_app = Usuarios()

        if opc == 1:
            registro = ["0", "0", "0", "0", "0"]
            print("ID é autoincrementado")
            registro[0] = str(input("Digite o nome do usuário: "))
            registro[1] = str(input("Digite o cpf: "))
            registro[2] = str(input("Digite o email: "))
            registro[3] = str(input("Digite o telefone: "))
            registro[4] = str(input("Digite a senha: "))
            usuario_app.insertUsuario(registro[0], registro[1], registro[2], registro[3], registro[4])
        elif opc == 2:
            v_idusuario = int(input("Digite o id do usuário: "))
            usuario_app.selectUsuario(v_idusuario)
        elif opc == 3:
            v_idusuario = int(input("Digite o id do usuário: "))
            lista = ["0", "0", "0", "0", "0"]
            lista[0] = str(input("Digite o novo nome do usuário: "))
            lista[1] = str(input("Digite o novo cpf: "))
            lista[2] = str(input("Digite o novo email: "))
            lista[3] = str(input("Digite o novo telefone: "))
            lista[4] = str(input("Digite a nova senha: "))
            usuario_app.updateUsuario(lista[0], lista[1], lista[2], lista[3], lista[4], v_idusuario)
        elif opc == 4:
            v_idusuario = int(input("Digite o id do usuário: "))
            usuario_app.deleteUsuario(v_idusuario)
        elif opc == 5:
            print("Fechando o programa...")
            time.sleep(2)

        # print("\n" * os.get_terminal_size().lines)


main()
