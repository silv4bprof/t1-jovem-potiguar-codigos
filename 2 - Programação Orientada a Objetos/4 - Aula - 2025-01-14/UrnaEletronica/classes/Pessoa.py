class Pessoa:
    def __init__(self, nome: str, cpf: str):
        # Atributos -> Características
        self.__nome = nome  # privado (__)
        self.__cpf = cpf  # privado

    # Método -> Comportamento
    def se_apresente(self) -> None:
        print(f"Nome: {self.__nome}\nCPF: {self.__cpf}")

    # Getters (pegar valor do atributo)
    # pegar_nome, exibir_nome
    def get_nome(self) -> str:
        return f"{self.__nome}"

    # pegar_cpf, exibir_cpf
    def get_cpf(self) -> str:
        return f"{self.__cpf}"

    # Setters (atribuir valor ao atributo)
    # Atribuir nome
    def set_nome(self, novo_nome: str):
        self.__nome = novo_nome

    # Atribuir cpf
    def set_cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf
