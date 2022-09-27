from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Conta Corrente
print('----- CONTA CORRENTE ----')
cc = ContaCorrente()
cc.cadastrar('12436-9', 7844, 133, 0, True)
print(cc.imprimriInformacoes())

print('-' * 30)


cc.depositar(450)
print(cc.imprimriInformacoes())

print('-' * 30)


cc.sacar(50)
print(cc.imprimriInformacoes())

########################################

# Conta Poupança
print('----- CONTA POUPANÇA ----')
cp = ContaPoupanca()
cp.cadastrar('00000-1', 5556, 144, 0, True)
print(cp.imprimriInformacoes())

print('-' * 30)

cp.depositar(500)
print(cp.imprimriInformacoes())

print('-' * 30)

cp.sacar(100)
print(cp.imprimriInformacoes())