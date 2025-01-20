from classes.Pessoa import Pessoa
from classes.Partido import Partido


class Candidato(Pessoa):  # político
    def __init__(self, nome: str, cpf: str, partido: Partido, numero: int):
        super().__init__(nome, cpf)
        self.__partido = partido
        self.__numero = numero

    def get_partido(self) -> Partido:
        # retorna a classe Partido de Candidato
        return self.__partido

    def get_numero(self):
        return self.__numero

    def se_apresente(self):
        print(f"{self.get_nome()}")
        print(f"{self.__partido.get_nome()} - {self.__partido.get_numero()}")
        print(f"Número: {self.__numero}")

    def __str__(self):
        return f"{self.get_partido().get_sigla().ljust(4)} - {self.__numero} - {self.get_nome()}"
