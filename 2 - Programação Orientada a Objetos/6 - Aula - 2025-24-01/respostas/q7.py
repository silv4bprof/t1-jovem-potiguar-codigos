# Questão 7: Empregado com validação de salário
class Empregado:
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = None
        self.set_salario(salario)

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_salario(self) -> float:
        return self.__salario

    def set_salario(self, salario: float):
        try:
            if salario <= 0:
                raise ValueError("O salário deve ser maior que zero.")
            self.__salario = salario
        except ValueError as e:
            print(f"Erro: {e}")


# empregado = Empregado("Maria João", 0)
empregado = Empregado("João Maria", 1350.99)
print(f"{empregado.get_nome()} ganha R$ {empregado.get_salario():.2f}")