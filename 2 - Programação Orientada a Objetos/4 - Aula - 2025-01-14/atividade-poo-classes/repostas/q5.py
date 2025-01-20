class Produto:
    def __init__(self, nome: str, preco: float = 0.0):
        self.__nome = nome
        self.__preco = preco

    def dados_produto(self):
        if self.__preco > 0:
            return f"O {self.__nome} custa R$ {self.__preco:.2f}"
        else:
            return f"O {self.__nome} não tem preço cadastrado."


produto1 = Produto("Notebook")
print(produto1.dados_produto())

produto2 = Produto("Celular", 2500)
print(produto2.dados_produto())
