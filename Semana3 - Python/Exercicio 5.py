import time


class ContaCorrente:

    def __init__(self, num_conta, nome_corre, saldo):
        self.num_conta = num_conta
        self.nome_corre = nome_corre
        self.saldo = saldo

    def alterar_nome(self):
        x = input("Digite o novo nome:\n")
        self.nome_corre = x

    def deposito(self):
        x = float(input("Digite o valor a ser depositado:\n"))
        self.saldo += x

    def saque(self):
        x = float(input("Digite o valor a ser sacado:\n"))
        self.saldo -= x


def main():

    conta01 = ContaCorrente(0, 0, 0)

    x = int(input("Insira o número da conta corrente:\n"))
    y = input("Insira o nome do correntista:\n")
    z = input("Gostaria de adicionar um saldo a conta? [s/n]\n")

    i = 0

    while i == 0:
        if z == 's':
            s = float(input("Digite este saldo:\n"))
            conta01.saldo = s
            i = 1
        elif z == "n":
            print("Não será adicionado saldo a esta conta")
            i = 1
        else:
            print("Opcão inválida\n")

    conta01.num_conta = x
    conta01.nome_corre = y

    while True:
        print("Digite 1 caso deseje alterar o nome")
        print("Digite 2 para efetuar um deposito")
        print("Digite 3 para fazer um saque")
        print("Digite 0 para sair")
        opcao = int(input("Opção:"))

        if opcao == 1:
            conta01.alterar_nome()
        elif opcao == 2:
            conta01.deposito()
        elif opcao == 3:
            conta01.saque()
        elif opcao == 0:
            print("Saindo...")
            time.sleep(2)
            break
        else:
            print("Opção indisponível tente outra vez\n")


main()
