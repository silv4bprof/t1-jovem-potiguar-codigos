class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def exibir_dados(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Ano: {self.__ano}")


# Instâncias de Carro()
carro1 = Carro("Toyota", "Corolla", 2020)
carro1.exibir_dados()

carro2 = Carro("FIAT", "Fastback", 2025)
carro2.exibir_dados()

carro3 = Carro("Honda", "Civic", 2010)
carro3.exibir_dados()
