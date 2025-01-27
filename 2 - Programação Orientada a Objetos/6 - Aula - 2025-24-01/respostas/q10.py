# Questão 10: Funcionario como herança de Pessoa
class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome


class Funcionario(Pessoa):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome)
        self.salario = None
        self.set_salario(salario)

    def set_salario(self, salario):
        try:
            if salario <= 0:
                raise ValueError("O salário deve ser maior que zero.")
            self.salario = salario
        except ValueError as e:
            print(f"Erro de Valor: {e}")
        except TypeError as e:
            print(f"Erro de Tipo: {e}")


func = Funcionario("Manoel", 0)
