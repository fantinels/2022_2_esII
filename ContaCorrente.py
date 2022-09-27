from turtle import clearstamp
from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta = None, agencia = None, codCliente = None, saldo = 0, cartaoCredito = False):
        super().__init__(numeroConta, agencia, codCliente, saldo)
        self.cartaoCredito = cartaoCredito

    def cadastrar(self):
        super().imprimriInformacoes()
        print(f'Cartão: {self.cartaoCredito}')

    def getCodCliente(self):
        super().getCodCliente()
        return self.codCliente

    def getSaldo(self):
        return self.saldo

    def __descontarTarifa(self):
        self.saldo -= 1.99

    def depositar(self, valorDepositado):
        super().depositar()
        self.saldo += valorDepositado
        self.__descontarTarifa()

    def sacar(self, valorSacado):
        self.saldo -= valorSacado
        self.__descontarTarifa()

    
        
