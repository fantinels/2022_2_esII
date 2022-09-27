from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta = None, agencia = None, codCliente = None, saldo = 0, cartaoCredito = False):
        super().__init__(numeroConta, agencia, codCliente, saldo)
        self.cartaoCredito = cartaoCredito

    def cadastrar(self, numeroConta, agencia, codCliente, saldo, cartaoCredito):
        self.__numeroConta = numeroConta
        self.__agencia = agencia
        self.codCliente = codCliente
        self.saldo = saldo
        self.cartaoCredito = cartaoCredito

    def __descontarTarifa(self):
        self.saldo -= 1.99

    def depositar(self, valorDepositado):
        super().depositar()
        self.saldo += valorDepositado
        self.__descontarTarifa()

    def sacar(self, valorSacado):
        self.saldo -= valorSacado
        self.__descontarTarifa()

    def imprimriInformacoes(self):
        return super().imprimriInformacoes() + f"""Cartão de Crédito: {self.cartaoCredito}"""

    
        
