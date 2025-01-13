class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, novo_nome) -> None:
        self.__nome = novo_nome


class Funcionario(Pessoa): ...


class Recutrador(Pessoa): ...


class Entrevista(Funcionario, Recutrador): ...
