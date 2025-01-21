class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        self.__nome = nome

    def set_idaded(self, idade):
        self.__nome = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    def saudacao(self) -> str:
        return f"Meu nome é {self.nome} e eu tenho {self.idade} anos!"


class PessoaChata(Pessoa):
    def __init__(self, nome: str, idade: int, nivelChatisse: int):
        super().__init__(nome, idade)
        self.__nivelChatisse = nivelChatisse

    @property
    def nivel_chatisse(self) -> int:
        return self.__nivelChatisse

    def saudacao(self) -> str:
        print(f"Meu nome é {self.nome}")
        print(f"Eu tenho {self.idade} anos!")
        print(f"Meu nível de chatisse é {self.nivel_chatisse}")


pessoa_chata = PessoaChata("Bruno", 28, 100)
pessoa_chata.saudacao()
