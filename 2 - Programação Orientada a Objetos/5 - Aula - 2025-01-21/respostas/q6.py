frutas = ["maçã", "banana", "laranja"]
try:
    indice = int(input("Digite o índice do item a ser removido: "))
    fruta_removida = frutas.pop(indice)
    print(f"A fruta {fruta_removida} foi removida da lista.")
except IndexError:
    print("Erro: Índice fora do alcance da lista.")
except ValueError:
    print("Erro: Você não digitou um número válido.")
