from classes import Partido
from classes import Candidato
from classes import Voto


class UrnaEletronica:
    def __init__(self):
        self.__candidatos: list[Candidato] = []
        self.__votos: list[Voto] = []
        self.__inicializar()

    def __inicializar(self):
        pt = Partido(13, "pt")
        candidato_pt = Candidato("Fernando Haddad", pt)
        pl = Partido(22, "pl")
        candidato_pl = Candidato("Jair Bolsonaro", pl)
        self.__candidatos.append(candidato_pt)
        self.__candidatos.append(candidato_pl)
        # self.__secao = 123
        # self.__zona = 321

    def adiciona_voto(self, voto: Voto):
        self.__votos.append(voto)

    def listar_votos(self, candidado: Candidato = None) -> list[Voto]:
        if candidado != None:
            votos_candidato: list[Voto] = []
            for voto in self.__votos:
                if (
                    voto.get_candidato().get_partido().get_numero()
                    == candidado.get_partido().get_numero()
                ):
                    votos_candidato.append(voto)
            return votos_candidato
        else:
            return self.__votos

    def recuperar_candidato(self, numero: int) -> Candidato:
        for candidato in self.__candidatos:
            numero_candidato = candidato.get_partido().get_numero()
            if numero_candidato == numero:
                return candidato  # se achou o candidato, não precisa continuar

        raise Exception("Candidato não existe na base!")

    def recuperar_candidatos(self) -> list[Candidato]:
        candidatos_recuperados: list[Candidato] = []
        for candidato in self.__candidatos:
            candidatos_recuperados.append(candidato)

        if len(candidatos_recuperados) == 0:
            raise Exception("Não existem candidatos na base!")

        return candidatos_recuperados
