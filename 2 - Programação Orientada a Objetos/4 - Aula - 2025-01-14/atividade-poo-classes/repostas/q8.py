from abc import ABC, abstractmethod


# receita de funcionário
class Funcionario(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome: str, salario_fixo: float):
        super().__init__(nome)
        self.salario_fixo = salario_fixo

    def calcular_salario(self):
        return self.salario_fixo


class Operador(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_por_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora


# Exemplo de uso
gerente = Gerente("Maria", 5000)
operador = Operador("José", 20, 50)

print(f"Salário do gerente {gerente.nome}: R${gerente.calcular_salario():.2f}")
print(f"Salário do operador {operador.nome}: R${operador.calcular_salario():.2f}")
