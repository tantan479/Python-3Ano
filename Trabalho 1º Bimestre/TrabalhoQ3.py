# Pedro Macedo Caetano

# 3. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

# a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
# no tanque.
# b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível
# de combustível no tanque de gasolina.
# d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# e. Forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:

    def __init__(self, consumo, combustivel=0):
        self.combustivel = combustivel
        self.consumo = consumo

    def definirconsumo(self):
        troca = input("Deseja mudar o consumo de combustível atual {} km/l? [s/n]".format(self.consumo))

        if troca == "s":
            novoconsumo = input("\n> Digite o novo consumo: ")
            self.consumo = novoconsumo
        else:
            print("Mantendo a consumo original de {} km/l.".format(self.consumo))

    def andar(self):
        possib = input("\nDeseja andar com o carro? [s/n]")

        if possib == "s":
            dist = int(input("\n> Digite a distância percorrida, em km: "))
            self.combustivel = self.combustivel - (dist / self.consumo)
        else:
            print("Mantendo o carro em lugar!")

    def obtergasolina(self):
        print("\nO total de combustível atual é de {} litros.".format(self.combustivel))

    def adicionargasolina(self):
        possi = input("\nDeseja adicionar combustível? [s/n]")

        if possi == "s":
            novo = int(input("\n> Digite a quantidade de combustível, em litros: "))
            self.combustivel += novo
        else:
            print("Mantendo o combustível original de {} litros".format(self.combustivel))


def limpa(x):
    print("\n" * x)


def main():
    consumo = int(input("Digite o consumo do carro, em km/l: "))

    carro01 = Carro(consumo, 0)

    while True:
        print("1 - Definir consumo")
        print("2 - Mostrar Gasolina")
        print("3 - Adicionar gasolina")
        print("4 - Andar")
        print("5 - Sair do programa")
        opc = input("Selecione uma opção: ")

        if opc == "1":
            limpa(10)
            carro01.definirconsumo()
        elif opc == "2":
            limpa(10)
            carro01.obtergasolina()
        elif opc == "3":
            limpa(10)
            carro01.adicionargasolina()
        elif opc == "4":
            limpa(10)
            carro01.andar()
        elif opc == "5":
            print("Encerrando programa.")
            limpa(10)
            break
        else:
            print("\nSelecione uma opção válida!!!")


main()
