import math


# Pertence a uma classe? Matematica  (operações matematicas dentro do contexto do meu programa)

class Matematica:
    def __init__(self, x = 0): # dando uma definição inicial, self é ele mesmo, quem é ele mesmo? È matematica
        self.x = x  # O atributo é x, as funções são os metodos

    def maior(self, x):
        if x > 5:
            print("O número é maior do que 5")  # TRUE
        else:
            print("O numero é menor ou igual a 5")  # FALSE

    def imprimeParidade(self, x):
        if x % 2 == 0:
            print("O número digitado é par!")
        else:
            print("O numero digitado é impar!")

    def imprimeLogaritmo(self, x):
        if x <= 0:
            print("Apenas números POSITIVOS!!!!")
            return
        resultado = math.log(x)
        print("O log de ", x, " é: ", resultado)


matematica = Matematica()
opcao = 0

while opcao !=9:
    print()
    print("1 - Verificar se o numero é maior que 5")
    print("2 - Verificar se o numero é par")
    print("3 - Logaritmo")
    print("9 - Encerrar")
    opcao = int(input("Escolha uma opcao:"))

    if opcao == 1:
        x = int(input("Digite o numero para verificacao"))  # input pega str por isso conventi para int
        matematica.maior(x)
    elif opcao == 2:
        x = int(input("Digite o numero para verificacao"))
        matematica.imprimeParidade(x)
    elif opcao == 3:
        x = int(input("Digite um numero para extrairmos o logaritmo"))
        matematica.imprimeLogaritmo(x)
