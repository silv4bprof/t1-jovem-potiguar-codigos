from abc import ABC, abstractmethod

# receita de pessoa


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        pass


class PessoaChata(Pessoa):
    def __init__(self, nome: str, idade: int, lv_chatisse: int):
        super().__init__(nome, idade)
        self.lv_chatisse = lv_chatisse

    def saudacao(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Lv Chatisse: {self.lv_chatisse}%")


pessoa_chata = PessoaChata("Bruno", 28, 100)
pessoa_chata.saudacao()
