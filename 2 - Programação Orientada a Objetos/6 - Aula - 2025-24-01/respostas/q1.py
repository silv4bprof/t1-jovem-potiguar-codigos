# Questão 1: ContaBancaria
class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self) -> str:
        return self.__titular

    def set_titular(self, titular: str):
        self.__titular = titular

    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, saldo: float):
        try:
            if saldo < 0:
                raise ValueError("O saldo não pode ser negativo.")
            self.__saldo = saldo
        except ValueError as e:
            print(f"Erro de Valor: {e}")


# Caso correto
cb = ContaBancaria("Bruno Silva", 2000)
print("Dados da Conta")
print(f"Titular: {cb.get_titular()}")
print(f"Saldo: {cb.get_saldo()}")

# forcando Exception
cb = ContaBancaria("Marcos Silva")
print("\nDados da Conta")
print(f"Titular: {cb.get_titular()}")
print(f"Saldo: {cb.get_saldo()}")
cb.set_saldo("-2000.0")
