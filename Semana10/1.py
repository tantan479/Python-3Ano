class ContaInvestimento:

    def __init__(self, numero, nome_titular, taxa_juros, saldo=0.0):
        self.numero = numero
        self.alterarnome(nome_titular)
        self.taxa_juros = taxa_juros
        self.saldo = saldo

    def alterar_nome(self, nome_titular):
        self.nome_titular = nome_titular

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def juros(self):
        self.saldo += (self.saldo*(self.taxa_juros/100))
