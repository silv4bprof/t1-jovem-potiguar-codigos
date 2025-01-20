class Partido:
    def __init__(self, nome: str, sigla: str, numero: int):
        self.__nome = nome
        self.__sigla = sigla
        self.__numero = numero
        self.__cnpj = "12.123.123/0001-12"

    def set_cnpj(self, novo_cnpj: str):
        self.__cnpj = novo_cnpj

    def get_nome(self) -> str:
        return self.__nome

    def get_numero(self) -> int:
        return self.__numero

    def get_cnpj(self) -> str:
        return self.__cnpj

    def get_sigla(self) -> str:
        return self.__sigla

    def get_informacao(self):
        return f"{self.__numero} - {self.__nome} - {self.__cnpj}"
