#Questão 2 da atividade, feita por Raphael Figueiredo Secchin IMI-3

class BombaCombustivel:

    def __init__(self, tipoCombustivel = 'a', valorLitro = 0, quantidadeCombustivel = 0, abastecimento1 = 0, abastecimento2 = 0 ):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        self.abastecimento1 = abastecimento1
        self.abastecimento2 = abastecimento2

    def abastecerPorValor(self, vLitro, valor):
        print("\nA quantidade de combustível é: {} L".format(float(valor) / float(self.valorLitro)))
        self.abastecimento1 = valor / vLitro

    def abastecerPorLitro(self, qComb):
        print("\nO valor a ser pago será: {} reais".format(float(qComb) / float(self.valorLitro)))

        self.abastecimento2 = qComb

    def alterarValor(self, opc2):
        if opc2 == 1:
            self.valorLitro = int(input("\nDigite o novo valor do litro de combustível: "))

            vLitro = self.valorLitro

            print("\nValor alterado com sucesso!!!\nO novo valor é: {}".format(vLitro))

    def alterarCombustivel(self, opc2):
        if opc2 == 'S':
            self.tipoCombustivel = input("Digite o novo tipo de combustível: ")

            print("\nO novo tipo de combustível é: {}".format(self.tipoCombustivel))

    def alterarQuantidadeCombustivel(self, qtdComb, opc3):
        if opc3 == 'S':
            op = 0
            while op != 1:
                self.quantidadeCombustivel = qtdComb

                self.quantidadeCombustivel = self.quantidadeCombustivel - (self.abastecimento1 + self.abastecimento2)
                adicionar = float(input("Digite quantos litros de combustível serão adicionados na bomba: "))

                if (self.quantidadeCombustivel + adicionar) <= qtdComb:
                    print("Foram adicionados: {}".format(adicionar), "\nAgora tem {} litros na bomba".format(self.quantidadeCombustivel + adicionar))
                else:
                    print("Valor inválido, pois ultrapassará o máximo de combustível")
                    op = 1

    def combustivelRestante(self, qtdComb):
        self.quantidadeCombustivel = qtdComb

        if self.quantidadeCombustivel != 0:
            res = self.quantidadeCombustivel - (self.abastecimento1 + self.abastecimento2)
            if res > 0:
                print("Na bomba tem {} litros restantes".format(res))
            else:
                print("Não há combustível na bomba")

def limpa(x):
    print("\n" * x)

def menu():
    opc = 0
    while opc != 1 and opc != 2 and opc != 3 and opc!= 4:
        print("+===================== Menu =====================+")
        print("1 - Abastecer pelo valor de combustível")
        print("2 - Abastecer por litro de combustível")
        print("3 - Quantidade de combustível restante na bomba")
        print("4 - Sair do programa")
        print("+================================================+")
        opc = int(input("Selecione uma opção: "))

    return opc

def main():
    comb01 = BombaCombustivel()
    opc0 = 0
    while opc0 != 4:
        limpa(2)
        opc = menu()

        if opc == 1:

          tipoCombustivel = input("Informe o tipo de combustível: ")

          opc2 = input("Em caso de erro, deseja alterar o tipo de combustível? [S/N]")
          if opc2 == 'S' or opc2 == 'N':
              comb01.alterarCombustivel(opc2)
          else:
                while opc2 != 'N' or opc2 != 'S':
                    print("\nERRO!!! Digite uma opção válida")
                    opc2 = input("Deseja alterar o tipo de combustível? [S/N]")
                    if opc2 == 'S':
                        comb01.alterarCombustivel()
                    elif opc2 == 'N':
                        break

          vLitro = float(input("\nDigite o valor do litro deste combustível: "))
          comb01.valorLitro = vLitro
          opc2 = input("Em caso de erro, deseja alterar o valor do combustível? [S/N]")

          if opc2 == 'S' or opc2 == 'N':
              comb01.alterarValor(vLitro, opc2)
          else:
              while opc2 != 'S' or opc2 != 'N':
                  print("\nERRO!!! Digite uma opção válida")
                  opc2 = input("Deseja alterar o valor deste combustível? [S/N]")
                  if opc2 == 'S':
                      comb01.alterarValor(vLitro)
                  elif opc2 == 'N':
                      break
          valor = float(input("\nAgora, digite o valor que foi colocado por litro de combustível: "))
          comb01.abastecerPorValor(vLitro, valor)

        elif opc == 2:

            opc2 = 'S'
            while opc2 == 'S':
                tipoCombustivel = input("Informe o tipo de combustível: ")

                opc2 = input("Em caso de erro, deseja alterar o tipo de combustível? [S/N]")

                if opc2 == 'S':
                    comb01.alterarCombustivel()
                break
            vLitro = float(input("\nDigite o valor do litro deste combustível: "))
            comb01.valorLitro = vLitro
            opc2 = input("Em caso de erro, deseja alterar o valor do combustível? [S/N]")

            if opc2 == 'S' or opc2 == 'N':
                comb01.alterarValor(vLitro, opc2)
            else:
                while opc2 != 'S' or opc2 != 'N':
                    print("\nERRO!!! Digite uma opção válida")
                    opc2 = input("Deseja alterar o valor deste combustível? [S/N]")
                    if opc2 == 'S' or opc2 == 's':
                        comb01.alterarValor(vLitro)
                    elif opc2 == 'N' or opc2 == 'n':
                        break
            qComb = int(input("\nDigite a quantidades de litros deste combustível que foi colocado no carro: "))
            comb01.abastecerPorLitro(vLitro, qComb)

        elif opc == 3:
            qtdComb = float(input("\nDigite a quantidade máxima de litros que cabe na bomba: "))

            comb01.combustivelRestante(qtdComb)

            opc3 = input("\nDeseja adicionar mais combustível na bomba? [S/N]")
            if opc3 == 'S' or opc3 == 'N':
                comb01.alterarQuantidadeCombustivel(qtdComb, opc3)
            else:
                while opc3 != 'S' or opc3 != 'N':
                    print("\nERRO!!! Digite uma opção válida")
                    opc3 = input("Deseja alterar a quantidade de combustível? [S/N]")
                    if opc3 == 'S':
                        comb01.alterarQuantidadeCombustivel(qtdComb)
                    elif opc3 == 'N':
                        break
        elif opc == 4:
         opc0 = 4
         print("Programa Finalizando...")

        else:
            print("Escolha uma opção válida")

main()