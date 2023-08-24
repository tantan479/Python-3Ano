class Pai:
    atributoPai = 100

    def __init__(self):
        print("Construtor - Chamando a classe Pai!!!")

    def set_atributo_pai(self, atributo):
        Pai.atributoPai = atributo

    def get_atributo_pai(self):
        print("Atributo Pai: ", Pai.atributoPai)

    def metodo_pai(self):
        print("Chamada ao método da classe Pai!!!")


class Mae:
    # atributoMae = 200

    def __init__(self, atributo_mae):
        print("Construtor - Chamando a classe Mãe!!!")
        self.atributoMae = atributo_mae

    def set_atributo_mae(self, atributo):
        Pai.atributoPai = atributo

    def get_atributo_mae(self):
        print("Atributo Mae: ", Mae.atributoMae)

    def metodo_mae(self):
        print("Chamada ao método da classe Mae!!!")


class Filha(Mae):

    def __init__(self, atributo_mae):
        print("Chamando o construtor da classe filha")
        # Pai.__init__(self)  # Invoco o construtor da classe pai para ela mesma
        # super().set_atributo_mae(200)  # estou indo direto na classe a qual eu herdei
        super().__init__(atributo_mae)  # chamando o construtor da super classe


# f = Filha() , dessa forma não funciona, pois o init do super precisa de um valor
f = Filha(200)  # assim funciona
# f.metodo_pai isto não funciona, pois Filha não herdou nada de pai
