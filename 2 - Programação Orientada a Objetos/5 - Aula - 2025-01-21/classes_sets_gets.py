class Pessoa:
    def __init__(self, nome: str = None, idade: int = None):
        self.__nome = nome
        self.__idade = idade

    # setters e getters
    # setters
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_idade(self, idade: int):
        self.__idade = idade

    def get_nome(self) -> str:
        return self.__nome

    def get_idade(self) -> int:
        return self.__idade


pessoa = Pessoa()
# set
pessoa.set_nome("Bruno Silva")
pessoa.set_idade(28)

# get
print(f"Nome: {pessoa.get_nome()}")
print(f"Idadae: {pessoa.get_idade()}")
