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
    atributoMae = 200

    def __init__(self):
        print("Construtor - Chamando a classe Mãe!!!")

    def set_atributo_mae(self, atributo):
        Pai.atributoPai = atributo

    def get_atributo_mae(self):
        print("Atributo Mae: ", Mae.atributoMae)

    def metodo_mae(self):
        print("Chamada ao método da classe Mae!!!")


class Filho(Pai, Mae):  # Filho esta herdando os metodos e atributos de pai e mãe por meio de herança múltipla
    atributoFilho = 300  # Este atributo pertence somente a Filho

    def __init__(self):
        print("Construtor - Chamando a classe Filho!!!")

    def metodo_filho(self):  # Este método pertence somente a Filho
        print("Chamada ao método da classe Filho!!!")

    def metodo_pai(self):
        print("Chamada ao método da classe filho - Sobrescrito")  # Isto sobrescreve o metodo_pai da classe pai


class Neta(Filho):  # Neta herda de filho que herda de pai e mae
    atributoNeto = 10

    def __init__(self):
        print("Construtor - Classe Neta!!!")


f = Filho()
f.get_atributo_mae()
f.set_atributo_mae(500)  # Isto altera o atributo da classe mãe, caso o set atributo de pai e mãe
# tiverem o mesmo nome ira funcionar apenas o da primeira classe coloca em filho. Ex.: Filho(Pai, Mae), neste caso
# funcionario apenas o do pai
n = Neta()
n.set_atributo_mae(1000)  # Sim! Isto funciona
n.get_atributo_mae()
f.metodo_filho()
f.metodo_pai()

p = Pai()
p.metodo_pai()  # assim chama o metodo_pai da classe pai

