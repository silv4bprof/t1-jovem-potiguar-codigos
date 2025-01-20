class Endereco:
    def __init__(self, rua: str, cidade: str, estado: str):
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado

    def get_rua(self) -> str:
        return self.__rua

    def get_cidade(self) -> str:
        return self.__cidade

    def get_estado(self) -> str:
        return self.__estado


class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: Endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    def exibir_dados(self):
        print(f"Dados Pessoa")
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print("+=" * 10)
        print("Dados Endereco Pessoa")
        print(f"Rua: {self.__endereco.get_rua()}")
        print(f"Cidade: {self.__endereco.get_cidade()}")
        print(f"Estado: {self.__endereco.get_estado()}")


endereco = Endereco("Rua A", "São Paulo", "SP")
pessoa = Pessoa("João", 30, endereco)
pessoa.exibir_dados()
