class Bola:

    def __init__(self, cor="sem cor", circunferencia = 0, material="sem material"):  # inicio o objeto com certos valore
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        troca = input("Deseja mudar a cor atual {}? [s/n]".format(self.cor))
        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Digite a nova cor: ")
            self.cor = nova_cor
        else:
            print("Mantendo a cor original! {}".format(self.cor))

    def mostra_cor(self):
        print("\nAcor atual é {}".format(self.cor))


def main():
    bola01 = Bola("Azul", 20, "Aço")

    while True:
        bola01.mostra_cor()
        bola01.troca_cor()

        continuar = input("Deseja continuar? [s/n]")
        continuar = continuar[0].lower()

        if continuar == "n":
            break

    bola01.mostra_cor()


main()
