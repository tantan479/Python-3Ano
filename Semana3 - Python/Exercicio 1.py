class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print("A cor é: ", self.cor)


bola01 = Bola('Azul', 20, 'Aço')
bola01.mostra_cor()

bola01.troca_cor('Vermelho')
bola01.mostra_cor()
