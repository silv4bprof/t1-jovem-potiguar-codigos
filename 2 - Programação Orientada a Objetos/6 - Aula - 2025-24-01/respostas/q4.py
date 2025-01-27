# Questão 4: Produto com validação de preço
class PrecoInvalido(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem


class Produto:
    def __init__(self, nome: str, preco: float = 0.0):
        self.__nome = nome
        self.__preco = None
        self.set_preco(preco)

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float):
        try:
            if preco < 0:
                raise PrecoInvalido("O preço deve ser maior que zero.")
            self.__preco = preco
        except PrecoInvalido as e:
            print(f"Erro de Preço: {e}")
        except ValueError as e:
            print(f"Erro de Valor: {e}")
        except TypeError as e:
            print(f"Erro de Tipo: {e}")


# produto = Produto("Fardo de Arroz", 40.00)
# produto.set_preco(-50.00)

produto = Produto("Fardo de Arroz")
