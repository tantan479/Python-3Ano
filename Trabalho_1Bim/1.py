"""
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um
objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os
valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

import time


class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_ponto(self):
        print("X: {}; Y: {}".format(self.x, self.y))


class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self, vert_part):
        x_centro = (self.largura/2) + vert_part.x
        y_centro = (self.altura/2) + vert_part.y
        centro = Ponto(x_centro, y_centro)
        return centro


def main():
    print("Digite as coordenadas do vértice(inferior esquerdo) de partida para o retângulo:")
    x = float(input("X: "))
    y = float(input("Y: "))

    vert_part = Ponto(x, y)

    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    retangulo01 = Retangulo(largura, altura)

    while True:
        print("\nDigite 1 para alterar o valor do retângulo")
        print("Digite 2 para encontrar o centro do retângulo")
        print("Digite 0 para sair")
        opcao = int(input("Opção: "))

        if opcao == 1:
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            print("Valores alterados com sucesso")
            retangulo01 = Retangulo(largura, altura)
        elif opcao == 2:
            if retangulo01.largura > 0 and retangulo01.altura > 0:
                centro = retangulo01.encontrar_centro(vert_part)
                print("O centro do retângulo é: ({}; {})". format(centro.x, centro.y))
            else:
                print("Valor(es) usado(s) em retângulo é/são inválido(s)")
        elif opcao == 0:
            print("Saindo...")
            time.sleep(2)
            break
        else:
            print("Valor digitado é inválido")


main()
