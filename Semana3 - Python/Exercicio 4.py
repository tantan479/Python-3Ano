import time


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

    def emagrecer(self, diminuir):
        self.peso -= diminuir


def main():

    print("Pessoa:\n")
    nome = input("Digite o nome da pessoa:\n")
    idade = int(input("Digite a idade da pessoa:\n"))
    peso = float(input("Digite o peso(Kg) da pessoa:\n"))
    altura = float(input("Digite a altura(m) da pessoa\n"))

    pessoa = Pessoa(nome, idade, peso, altura)

    opcao = 1

    while opcao != 0:
        print("Digite 1 caso deseje envelhecer 1 ano")
        print("Digite 2 caso deseje engordar")
        print("Digite 3 caso deseje emagrecer")
        print("Digite 0 para sair")
        opcao = int(input("Opção:"))

        if opcao == 1:
            pessoa.envelhecer()
        elif opcao == 2:
            x = int(input("Digite quantos quilos voce engordou:\n"))
            pessoa.engordar(x)
        elif opcao == 3:
            x = int(input("Digite quantos quilos voce emagreceu:\n"))
            pessoa.emagrecer(x)
        elif opcao == 0:
            print("Saindo...")
            time.sleep(2)
            opcao = 0
        else:
            print("Opção indisponível tente outra vez\n")


main()
