from datetime import datetime


class Partido:
    def __init__(self, numero: int, nome: str):
        self.__numero = numero
        self.__nome = nome

    def get_nome(self):
        return f"{self.__nome.upper()}"

    def get_numero(self):
        return int(self.__numero)

    def __str__(self):
        return f"{self.__nome} - {self.__numero}"


class Candidato:
    def __init__(self, nome: str, partido: Partido):
        self.__nome = nome
        self.__partido = partido

    def __str__(self) -> str:
        return f"{self.__nome} - {self.__partido.get_nome()}"

    def get_nome(self) -> str:
        return f"{self.__nome}"

    def get_partido(self) -> Partido:
        return self.__partido


class Eleitor:
    def __init__(self, nome: str, titulo_eleitor: str):
        self.__nome = nome
        self.__titulo_eleitor = titulo_eleitor

    def __str__(self):
        return f"{self.__nome} - {self.__titulo_eleitor}"

    def get_nome(self):
        return f"{self.__nome}"


class Voto:
    def __init__(self, data: datetime, eleitor: Eleitor, candidato: Candidato):
        self.__data = data
        self.__eleitor = eleitor
        self.__candidato = candidato

    def __str__(self):
        data = self.__data
        eleitor = self.__eleitor.get_nome()
        candidato = self.__candidato.get_nome()
        return f"{eleitor} - {candidato} - {data.strftime("%d/%m/%Y %H:%M:%S")}"

    def get_candidato(self) -> Candidato:
        return self.__candidato
