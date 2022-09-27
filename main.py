from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Conta Corrente
print('----- CONTA CORRENTE ----')
cc = ContaCorrente('12436-9', 7844, 133, 0, True)
cc.cadastrar()

print('-' * 30)

cc.depositar(450)
cc.cadastrar()

print('-' * 30)

cc.sacar(50)
cc.cadastrar()

########################################

# Conta Poupança
print('----- CONTA POUPANÇA ----')
cp = ContaPoupanca('00000-1', 5556, 144, 0, True)
cp.cadastrar()

print('-' * 30)

cp.depositar(500)
cp.cadastrar()

print('-' * 30)

cp.sacar(100)
cp.cadastrar()