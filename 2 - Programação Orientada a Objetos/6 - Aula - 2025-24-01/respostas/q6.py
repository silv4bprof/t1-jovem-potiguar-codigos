from abc import ABC, abstractmethod


# Questão 6: Conta, ContaCorrente e ContaPoupanca
class Conta(ABC):
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def sacar(self, valor: float):
        pass


class ContaCorrente(Conta):
    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor):
        if valor + 2.50 > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor + 2.50


class ContaPoupanca(Conta):
    def __init__(self, titular: str, saldo: float = 0.0):
        super().__init__(titular, saldo)
        self.saques_gratis = 3

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if self.saques_gratis > 0:
            if valor > self.saldo:
                print("Saldo insuficiente.")
            else:
                self.saldo -= valor
                self.saques_gratis -= 1
        else:
            if valor + 5.00 > self.saldo:
                print("Saldo insuficiente.")
            else:
                self.saldo -= valor + 5.00


print("Conta Corrente")
cc = ContaCorrente("Bruno Silva", 5000)
print(f"Saldo de {cc.titular}: {cc.saldo}")
cc.depositar(5000)
print(f"Saldo de {cc.titular}: {cc.saldo}")
cc.sacar(5000)  # valor do saque + R$ 2,50
print(f"Saldo de {cc.titular}: {cc.saldo}")


print("\nConta Poupança")
cp = ContaPoupanca("Manoela Medeiros", 2000)
cp.depositar(3000)
print(f"Saldo de {cp.titular}: {cp.saldo}")
cp.sacar(1000)
cp.sacar(1000)
cp.sacar(1000)
print(f"Saldo de {cp.titular}: {cp.saldo}")
cp.sacar(1000)
print(f"Saldo de {cp.titular}: {cp.saldo}")
