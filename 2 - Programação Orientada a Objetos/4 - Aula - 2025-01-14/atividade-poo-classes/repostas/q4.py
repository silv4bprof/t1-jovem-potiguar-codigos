class FormaGeometrica:
    def calcular_area(): ...


class Retangulo:
    def __init__(self, altura: int, largura: int):
        self.__altura = altura
        self.__largura = largura

    def calcular_area(self) -> int:
        return self.__largura * self.__altura


class Circulo:
    def __init__(self, raio: int):
        self.__raio = raio

    def calcular_area(self) -> int:
        return (self.__raio**2) * 3.14159


retangulo = Retangulo(5, 10)
circulo = Circulo(7)
print(retangulo.calcular_area())
print(circulo.calcular_area())
