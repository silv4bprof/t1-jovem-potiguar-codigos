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
        self.__titulo_eleitor = titulo_eleitor

    def se_apresente(self):
        print(f"Nome: {self.get_nome()}\nTítulo: {self.get_titulo()}")

    # Getters & Setters
    def get_titulo(self) -> str:
        return f"{self.__titulo_eleitor}"

    def set_titulo(self, novo_titulo_eleitor: str):
        self.__titulo_eleitor = novo_titulo_eleitor

    # sobreposição de método
    def __str__(self):
        return self.get_nome()


class Partido:
    def __init__(self, nome: str, numero: int):
        self.__nome = nome
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

    def get_informacao(self):
        return f"{self.__numero} - {self.__nome} - {self.__cnpj}"


class Candidato(Pessoa):
    def __init__(self, nome: str, cpf: str, partido: Partido, numero: int):
        super().__init__(nome, cpf)
        self.__partido = partido
        self.__numero = numero

    def get_partido(self) -> Partido:
        return self.__partido

    def se_apresente(self):
        print(f"{self.get_nome()}")
        print(f"{self.__partido.get_nome()} - {self.__partido.get_numero()}")
        print(f"Número: {self.__numero}")


class Voto:
    def __init__(self, eleitor: Eleitor, candidato: Candidato):
        self.__eleitor = eleitor
        self.__candidato = candidato

    def get_dados(self):
        return f"{self.__eleitor.get_nome()} votou em {self.__candidato.get_nome()}"


class Urna:
    """
    1. Informa o título de eleitor
    2. Pesquisa o candidato
    3. Guarda [titulo, numero_candidato]
    """

    def __init__(self):
        self.__votos_computados: list[Voto] = []

    def adicionar_voto(self, voto: Voto):
        self.__votos_computados.append(voto)

    def exibe_votos(self):
        for voto in self.__votos_computados:
            print(voto.get_dados())


if __name__ == "__main__":
    print("Partido(s)")
    pt = Partido("Partido dos Trabalhadores", 13)
    pt.set_cnpj("12.123.123/0001-13")

    pl = Partido("Partido Liberal", 22)
    pl.set_cnpj("52.854.789/0001-22")

    print(pt.get_informacao())
    print(pl.get_informacao())

    print("\nCandidatos(as)")
    candidato1 = Candidato("Manoel Tavares", "12345678998", pt, 13333)
    candidato2 = Candidato("Josefina Mendes", "78965412332", pl, 22222)

    candidato1.se_apresente()
    candidato2.se_apresente()

    print("-" * 10 + " Part. Candt. 2 " + "-" * 10)
    print(candidato2.get_partido().get_nome())
    print(candidato2.get_partido().get_numero())
    print(candidato2.get_partido().get_cnpj())

    print("\nEleitor(es)")
    eleitor = Eleitor("Manoel Medeiros Paiva", "85245696558", 78954655)
    eleitor.se_apresente()

    eleitor.set_nome("Manoel Medeiros")
    eleitor.se_apresente()

    # print(eleitor)
