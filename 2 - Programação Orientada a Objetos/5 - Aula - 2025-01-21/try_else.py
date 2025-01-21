from abc import ABC, abstractmethod


class Calculo(ABC):
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    @abstractmethod
    def calcular(self) -> float:
        pass


class Calculadora(Calculo):
    def __init__(self, num1: float, num2: float, operacao: str = ""):
        super().__init__(num1, num2)
        # operacoes -> +, -, *, /
        self.__operacao = operacao

    @property
    def operacao(self):  # get_operacao()
        return self.__operacao

    def calcular(self) -> float:
        resultado = 0.0
        if self.operacao == "+":
            resultado = self.num1 + self.num2
        elif self.operacao == "-":
            resultado = self.num1 - self.num2
        elif self.operacao == "*":
            resultado = self.num1 * self.num2
        elif self.operacao == "/":
            resultado = self.num1 / self.num2
        else:
            print("Nenhuma operacao selecionada.")
        return resultado


print("Cálculos Matemáticos\n")


try:
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    calculo = Calculadora(num1, num2)
    print(f"Resultado (sem operação): {calculo.calcular()}")
    calculo_soma = Calculadora(num1, num2, "+")
    print(f"\nResultado (soma): {calculo_soma.calcular()}")
    calculo_sub = Calculadora(num1, num2, "-")
    print(f"\nResultado (subtração): {calculo_sub.calcular()}")
    calculo_mult = Calculadora(num1, num2, "*")
    print(f"\nResultado (multiplicação): {calculo_mult.calcular()}")
    calculo_div = Calculadora(num1, num2, "/")
    print(f"\nResultado (divisão): {calculo_div.calcular()}")
except ValueError as e:
    print("Erro de Valor")
    print(f"Error Message: {e}")
except ZeroDivisionError as e:
    print("Erro de Divisão por 0")
    print(f"Error Message: {e}")
except NameError as e:
    print("Erro de Variável que não existe")
    print(f"Error Message: {e}")
finally:
    print("saindo ...")
