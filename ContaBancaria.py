from abc import ABCMeta, abstractmethod


class ContaBancaria(metaclass = ABCMeta):
    def __init__(self, numeroConta = None, agencia = None, codCliente = None, saldo = 0):
        self.__numeroConta = numeroConta
        self.__agencia = agencia
        self.codCliente = codCliente
        self.saldo = saldo

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def getCodCliente(self):
        pass

    @property
    def getNumeroConta(self):
        return self.__numeroConta

    @property
    def getAgencia(self):
        return self.__agencia

    def imprimriInformacoes(self):
        print(f'Número da Conta: {self.__numeroConta}\nAgência: {self.__agencia}\nCódigo do Cliente: {self.codCliente}\nSaldo atual: {self.saldo}')
