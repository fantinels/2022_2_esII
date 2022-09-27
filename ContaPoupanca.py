from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta = None, agencia = None, codCliente = None, saldo = 0, cartaoDebito = False):
        super().__init__(numeroConta, agencia, codCliente, saldo)
        self.cartaoDebito = cartaoDebito

    def cadastrar(self):
        super().imprimriInformacoes()
        print(f'Cartão de Débito: {self.cartaoDebito}')

    def getCodCliente(self):
        super().getCodCliente()
        return self.codCliente    

    def getSaldo(self):
        return self.saldo

    def __rendimentoMes(self):
        self.saldo = self.saldo + (self.saldo * 0.5 / 100)

    def depositar(self, valorDepositado):
        super().depositar()
        self.saldo += valorDepositado
        self.__rendimentoMes()

    def sacar(self, valorSacado):
        self.saldo -= valorSacado
        self.__rendimentoMes()
    