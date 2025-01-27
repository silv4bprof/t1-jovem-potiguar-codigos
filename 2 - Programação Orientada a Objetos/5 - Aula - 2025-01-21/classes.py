from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def saudacao(self):
        pass


class PessoaChata(Pessoa):
    def __init__(self, nome: str, idade: int, lv_chatisse: int):
        super().__init__(nome, idade)
        self.__lv_chatisse = lv_chatisse

    @property
    def lv_chatisse(self):
        return self.__lv_chatisse

    def saudacao(self):
        print(
            f"""
        Nome: {self.nome}
        Idade: {self.idade}
        Lv Chatisse: {self.lv_chatisse}%
        """
        )


pc = PessoaChata("Bruno Silva", 28, 100)
pc.saudacao()
