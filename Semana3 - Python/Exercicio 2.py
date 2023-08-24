import time


class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado
        print("Lado mudado com sucesso\n")

    def valor_lado(self):
        return self.lado

    def calcular_area(self):
        print("A area deste quadrado é: ", self.lado*self.lado, "\n")


def main():

    quadrado = Quadrado(0)
    opcao = 1

    while opcao != 0:
        time.sleep(1)
        print("Escolha:\n1-Mudar valor do lado\n2-Retornar valor do lado\n3-Calcular Área\n0-Sair")
        opcao = int(input("\nDigite uma opção: "))

        if opcao == 1:
            x = float(input("Digite o valor do lado: "))
            quadrado.mudar_lado(x)
        elif opcao == 2:
            print("O valor do lado é: ", quadrado.valor_lado(), "\n")
        elif opcao == 3:
            quadrado.calcular_area()
        elif opcao == 0:
            print("\nSaindo...")
            time.sleep(1)
            break
        else:
            print("Opção inválida, tente outra\n")


main()
