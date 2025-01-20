from classes.Voto import Voto


class Urna:
    def __init__(self):
        self.__votos_computados: list[Voto] = []

    def adicionar_voto(self, voto: Voto):
        self.__votos_computados.append(voto)

    def exibe_votos(self):
        if self.__votos_computados:
            for voto in self.__votos_computados:
                print(voto)
        else:
            print("Urna vazia!")
