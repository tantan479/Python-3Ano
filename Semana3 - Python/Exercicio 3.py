class Retangulo:

    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura

    def mudar_lados(self):
        nova_base = int(input("Digite a base:\n"))
        nova_altura = int(input("Digite a altura:\n"))
        self.base = nova_base
        self.altura = nova_altura

    def retornar_lados(self):
        print("Base: \n", self.base, "Altura: \n", self.altura)

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        return perimetro


def main():
    local = Retangulo()
    piso = Retangulo()
    rodape = Retangulo()

    print("Informe as medidas de um local:")
    local.mudar_lados()
    print("Informe as medidas do piso:")
    piso.mudar_lados()
    print("Informe apenas as medidas do rodapé:")
    rodape.mudar_lados()

    qtd_pisos = local.calcular_area() / piso.calcular_area()
    qtd_rodapes = local.calcular_perimetro()/rodape.base

    print("A quantidade de pisos é:\n", qtd_pisos)
    print("A quantidade de rodapés é:\n", qtd_rodapes)


main()
