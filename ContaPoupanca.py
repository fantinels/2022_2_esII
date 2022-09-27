from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta = None, agencia = None, codCliente = None, saldo = 0, cartaoDebito = False):
        super().__init__(numeroConta, agencia, codCliente, saldo)
        self.cartaoDebito = cartaoDebito

    def cadastrar(self, numeroConta, agencia, codCliente, saldo, cartaoDebito):
        self.__numeroConta = numeroConta
        self.__agencia = agencia
        self.codCliente = codCliente
        self.saldo = saldo
        self.cartaoDebito = cartaoDebito

    def __rendimentoMes(self):
        self.saldo = self.saldo + (self.saldo * 0.5 / 100)

    def depositar(self, valorDepositado):
        super().depositar()
        self.saldo += valorDepositado
        self.__rendimentoMes()

    def sacar(self, valorSacado):
        self.saldo -= valorSacado
        self.__rendimentoMes()

    def imprimriInformacoes(self):
        return super().imprimriInformacoes() + f"""Cartão Débito: {self.cartaoDebito}"""
    