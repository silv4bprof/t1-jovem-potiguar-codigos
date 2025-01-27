numeros = [10, 20, 30]
try:
    indice = int(input("Digite um índice: "))
    print(f"O número no índice {indice} é {numeros[indice]}")
except IndexError:
    print("Erro: Índice fora do alcance da lista.")
except ValueError:
    print("Erro: Você não digitou um número válido.")
