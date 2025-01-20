class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    # setters e getters
    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self) -> float:
        return self.__saldo

    def get_titular(self) -> str:
        return self.__titular

    # médotos da classe
    def saldo_atual(self):
        print(f"Saldo Atual: R$ {conta.get_saldo():.2f}")

    def depositar(self, valor: float):
        self.__saldo = self.__saldo + valor
        self.saldo_atual()

    def sacar(self, valor: float):
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
        else:
            print("Valor maior que o saldo!")
        self.saldo_atual()


conta = ContaBancaria("João", 1000)
conta.depositar(500)  # 1500
conta.sacar(200)  # 1300
