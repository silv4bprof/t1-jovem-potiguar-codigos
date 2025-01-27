# Questão 2: Classes abstratas Veiculo, Carro e Bicicleta
from abc import ABC, abstractmethod


# classe abstrata
class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass


# classe concreta
class Carro(Veiculo):
    pass

    def mover(self):
        print("O carro está se movendo.")


# classe concreta (com erro)
class Bicicleta(Veiculo):
    pass


try:
    try:
        carro = Carro()  # vai dar certo
    except Exception:
        print("Erro de instância (try-except interno).")
    else:
        print("Classe Carro instanciada com sucesso!")
    finally:
        print("Try-Except INTERNO finalizado.")
    veiculo = Bicicleta()  # vai dar errado (não tem o método mover)
except TypeError as e:
    print(f"Erro de Instância: {e}")
finally:
    print("Try-Except EXTERNO finalizado.")
