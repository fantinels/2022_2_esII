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

    @property
    def getNumeroConta(self):
        return self.__numeroConta

    @property
    def getAgencia(self):
        return self.__agencia

    def imprimriInformacoes(self):
        return f"""
        Número da Conta: {self.__numeroConta}
        Agência: {self.__agencia}
        Código do Cliente: {self.codCliente}
        Saldo atual: {self.saldo}
        """
