from classes.Eleitor import Eleitor
from classes.Candidato import Candidato


class Voto:
    def __init__(self, eleitor: Eleitor, candidato: Candidato):
        self.__eleitor = eleitor
        self.__candidato = candidato

    def get_dados(self):
        return f"{self.__eleitor.get_nome()} votou em {self.__candidato.get_nome()}"

    def get_eleitor(self) -> Eleitor:
        return self.__eleitor

    def get_candidato(self) -> Candidato:
        return self.__candidato

    def __str__(self):
        return f"{self.get_eleitor().get_nome()} votou em {self.get_candidato().get_nome()}"
