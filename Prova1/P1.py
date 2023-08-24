"""
Aluno: Renato Ribeiro Altoé

Faça uma classe chamada Restaurante. O método __init __ () para o restaurante deve armazenar dois atributos:
um nomeRestaurante e um tipoComida.

Faça um método chamado descricaoRestaurante() que imprime essas duas informações e um método chamado restauranteAberto()
que imprime uma mensagem indicando que o restaurante está aberto.

Faça uma instância chamada restaurante de sua classe Imprima os dois atributos individualmente e, em seguida, chame
os dois métodos.

"""


class Restaurante:

    def __init__(self, nomeRestaurante, tipoComida):
        self.nomeRestaurante = nomeRestaurante
        self.tipoComida = tipoComida

    def descricaoRestaurante(self):
        print("Nome do restaurante: ", self.nomeRestaurante,"\nTipo de comida: ", self.tipoComida)

    def restauranteAberto(self):
        print("O restaurante está aberto")


def main():

    restaurante = Restaurante('Casa Urbana', 'Brasileira')

    print("Imprimindo os atributos:")
    print("Nome do restaurante: ", restaurante.nomeRestaurante)
    print("Tipo de comida: ", restaurante.tipoComida)

    print("\nChamando os métodos:")
    restaurante.descricaoRestaurante()
    print("")
    restaurante.restauranteAberto()


main()
