from classes.Pessoa import Pessoa


# Herança: Eleitor herda de Pessoa
# Classe Filho(a)
class Eleitor(Pessoa):
    def __init__(self, nome: str, cpf: str, titulo_eleitor: int):
        super().__init__(nome, cpf)
        self.__titulo = titulo_eleitor

    def se_apresente(self):
        print("\nDados do Eleitor:\n")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Título: {self.get_titulo()}")

    # Getters & Setters
    def get_titulo(self) -> str:
        return f"{self.__titulo}"

    def set_titulo(self, novo_titulo_eleitor: str):
        self.__titulo = novo_titulo_eleitor

    # sobreposição de método
    def __str__(self):
        return f"__str__: {self.get_nome()}"
