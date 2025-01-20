from classes.Candidato import Candidato


class Pleito:
    def __init__(self):
        self.__candidatos: list[Candidato] = []

    def adicionar_candidato(self, candidato: Candidato):
        self.__candidatos.append(candidato)

    def exibir_candidatos(self):
        for candidato in self.__candidatos:
            print(candidato)

    def retorna_candidato(self, numero: int) -> Candidato | None:
        for candidato in self.__candidatos:
            if candidato.get_numero() == numero:
                return candidato
        return None
