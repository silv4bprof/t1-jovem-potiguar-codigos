class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        return f"{self.marca} {self.modelo}, Ano: {self.ano}"
    
class MeuCarro(Carro):
    ...

class SeuCarro(Carro):
    ...

class OutroCarro(Carro):
    ...
    
# Exemplo de uso
carro = Carro("Toyota", "Corolla", 2020)
print(carro.exibir_detalhes())

class Pessoa():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def exibe_pessoa(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}")