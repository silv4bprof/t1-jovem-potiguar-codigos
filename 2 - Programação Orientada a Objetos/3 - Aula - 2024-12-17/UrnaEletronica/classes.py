"""
    Urna Eletrônica Orientada a Objetos
"""


# Classe PAI/MÃE
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


# Herança: Eleitor herda de Pessoa
# Classe Filho(a)
class Eleitor(Pessoa):
    def __init__(self, nome: str, cpf: str, titulo_eleitor: int):
        super().__init__(nome, cpf)
        self.__titulo = titulo_eleitor

    def se_apresente(self):
        print(f"Nome: {self.get_nome()}\nTítulo: {self.get_titulo()}")

    # Getters & Setters
    def get_titulo(self) -> str:
        return f"{self.__titulo}"

    def set_titulo(self, novo_titulo_eleitor: str):
        self.__titulo = novo_titulo_eleitor

    # sobreposição de método
    def __str__(self):
        return f"__str__: {self.get_nome()}"


class Partido:
    def __init__(self, nome: str, sigla: str, numero: int):
        self.__nome = nome
        self.__sigla = sigla
        self.__numero = numero
        self.__cnpj = "12.123.123/0001-12"

    def set_cnpj(self, novo_cnpj: str):
        self.__cnpj = novo_cnpj

    def get_nome(self) -> str:
        return self.__nome

    def get_numero(self) -> int:
        return self.__numero

    def get_cnpj(self) -> str:
        return self.__cnpj

    def get_sigla(self) -> str:
        return self.__sigla

    def get_informacao(self):
        return f"{self.__numero} - {self.__nome} - {self.__cnpj}"


class Candidato(Pessoa):  # político
    def __init__(self, nome: str, cpf: str, partido: Partido, numero: int):
        super().__init__(nome, cpf)
        self.__partido = partido
        self.__numero = numero

    def get_partido(self) -> Partido:
        # retorna a classe Partido de Candidato
        return self.__partido

    def se_apresente(self):
        print(f"{self.get_nome()}")
        print(f"{self.__partido.get_nome()} - {self.__partido.get_numero()}")
        print(f"Número: {self.__numero}")

    def __str__(self):
        return f"{self.get_partido().get_sigla().ljust(4)} - {self.__numero} - {self.get_nome()}"


class Voto:
    def __init__(self, eleitor: Eleitor, candidato: Candidato):
        self.__eleitor = eleitor
        self.__candidato = candidato

    def get_dados(self):
        return f"{self.__eleitor.get_nome()} votou em {self.__candidato.get_nome()}"

    def get_eleitor(self) -> Eleitor:
        return self.__eleitor

    def get_candidato(self) -> Candidato:
        return self.__candidato

    def __str__(self):
        return f"{self.get_eleitor().get_nome()} votou em {self.get_candidato().get_nome()}"


class Pleito:
    def __init__(self):
        self.__candidatos: list[Candidato] = []

    def adicionar_candidato(self, candidato: Candidato):
        self.__candidatos.append(candidato)

    def exibir_candidatos(self):
        for candidato in self.__candidatos:
            print(candidato)


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
