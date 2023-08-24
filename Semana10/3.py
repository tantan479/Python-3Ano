class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def retornar_nome(self):
        print("O nome deste funcionário é: ", self.nome)

    def retornar_salario(self):
        print("O salário é: ", self.salario)

    def aumentar_salario(self, p):
        self.salario += self.salario*(p/100)
        print("Novo salário: ", self.salario)


def main():

    y = input("Digite o nome do funcionário: ")
    x = input("Digite seu salário: ")

    funcionario01 = Funcionario(y, x)

    print("\nMétodo - Retornar nome")
    funcionario01.retornar_nome()
    print("Método - Retornar salário")
    funcionario01.retornar_salario()

    z = input("\nGostaria de aumentar o seu salárío (s/n): ")
    if z == 's':
        p = int(input("Digite o valor em porcentagem: "))
        funcionario01.aumentar_salario(p)
    else:
        print("Obrigado por usar o programa")


main()
