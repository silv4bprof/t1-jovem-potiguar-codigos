# Questão 8: Estoque com manipulação de produtos]
class Produto:
    def __init__(self, nome: str, preco: float, codbar: str):
        self.__nome = nome
        self.__preco = preco
        self.__codbar = None
        self.set_codbar(codbar)

    def set_codbar(self, codbar):
        try:
            if len(codbar) != 8:
                raise Exception("Cód. Barra deve ter 8 digitos, apenas.")
            self.__codbar = codbar
        except Exception as e:
            print(f"Erro de Valor: {e}")

    def get_produto(self) -> str:
        return f"{self.__nome}\t{self.__preco}\t{self.__codbar}"


class Estoque:
    def __init__(self):
        self.produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self):
        try:
            if not self.produtos:
                raise IndexError("O estoque está vazio.")
            return self.produtos.pop()
        except IndexError as e:
            print(f"Erro: {e}")

    def listar_produtos(self):
        try:
            if not self.produtos:
                raise IndexError("O estoque está vazio.")
            else:
                for index, produto in enumerate(self.produtos, start=1):
                    print(index, produto.get_produto())
        except IndexError as e:
            print(f"Erro: {e}")


estoque = Estoque()

produto1 = Produto("Macarrão", 5.00, "23444345")
produto2 = Produto("Feijão", 4.50, "09876543")
produto3 = Produto("Margarina", 6.00, "12345678")
produto4 = Produto("Cachaça", 18.00, "22323123")

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)
estoque.adicionar_produto(produto4)

estoque.listar_produtos()
