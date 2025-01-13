class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibe_pessoa(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}")


class Dono(Pessoa):

    def __init__(self, nome, cpf, data_compra):
        super().__init__(nome, cpf)
        self.data_compra = data_compra

    def exibe_dono(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nCompra: {self.data_compra}")


pessoa = Pessoa("Bruno", "012.584.685-89")
pessoa.exibe_pessoa()

dono = Dono("Roberto", "018.856.857-89", "2025-01-13")
dono.exibe_dono()
