# Questão 8: Estoque com manipulação de produtos]
class Produto:
    ...
    # nome do produto: str
    # preco do produto: float
    # cód. barra: str (tamanho 8)


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: str):  # produto: Produto
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
                for produto in self.produtos:
                    print(produto)
        except IndexError as e:
            print(f"Erro: {e}")


estoque = Estoque()
estoque.adicionar_produto("Macarrão")
estoque.adicionar_produto("Feijão")
estoque.adicionar_produto("Margarina")
estoque.adicionar_produto("Cachaça")

# 4
print("\nEstoque Atual:")
estoque.listar_produtos()

# 3
print("\nEstoque Atual:")
estoque.remover_produto()
estoque.listar_produtos()

# 2
print("\nEstoque Atual:")
estoque.remover_produto()
estoque.listar_produtos()

# 1
print("\nEstoque Atual:")
estoque.remover_produto()
estoque.listar_produtos()

# 0
print("\nEstoque Atual:")
estoque.remover_produto()
estoque.listar_produtos()
