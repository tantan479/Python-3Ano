class Funcionario:

    funcCount = 0  # contar os funcionarios

    def __init__(self, nome, salario):  # instancia o objeto em memoria
        self.nome = nome
        self.salario = salario
        Funcionario.funcCount += 1

    def displayCount(self):  # retorna a quantidade de funcionarios
        print("Total de funcionários: %d" % Funcionario.funcCount)

    def displayFuncionario(self):
        print("Nome: ", self.nome, ", Salário: ", self.salario)  # mostra dele mesmo


funcionario01 = Funcionario("Carlos", 2000)  # criei um objeto baseado na classe funcionario
funcionario02 = Funcionario("Alice", 5000)

funcionario01.displayFuncionario()
funcionario02.displayFuncionario()

# Adionar atributos a um objeto em memória
funcionario01.idade = 45  # somente o objeto funcionario01 possui este atributo
funcionario01.idade = 26  # agora este objeto tambem possui a idade

funcionario02.idade = 27

hasattr(funcionario01, 'idade')  # retorna um booleano caso o objeto possui o atributo idade
getattr(funcionario01, 'nome')  # retorna o atributo nome do objeto funcionario01
setattr(funcionario01, 'nome', 'Pedro')  # altera o nome para Pedro
delattr(funcionario01, 'idade') # exclui o atributo idade

print("Total de funcionarios: %d" % Funcionario.funcCount)
funcionario01.displayCount()  # acesso diretamente a variavel
