class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.__nome} e eu tenho {self.__idade} anos de idade.")

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade


class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.__matricula = matricula

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.get_nome()}")
        print(f"eu tenho {self.get_idade()} anos de idade")
        print(f"minha matricula é {self.__matricula}")


pessoa = Pessoa("Bruno Silva", 28)
pessoa.cumprimentar()

estudante = Estudante("Ana", 21, "20230001")
estudante.cumprimentar()
