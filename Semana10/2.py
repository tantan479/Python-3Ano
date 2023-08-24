class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def retornar_nome(self):
        return self.nome

    def retornar_salario(self):
        return self.salario


def main():

    y = input("Digite o nome do funcionário: ")
    x = input("Digite seu salário: ")

    funcionario01 = Funcionario(y, x)

    print("\nMétodo - Retornar nome")
    nome = funcionario01.retornar_nome()
    print("O nome deste funcionário é: ", nome)
    print("Método - Retornar salário")
    salario = funcionario01.retornar_salario()
    print("O salário é: ", salario)


main()
