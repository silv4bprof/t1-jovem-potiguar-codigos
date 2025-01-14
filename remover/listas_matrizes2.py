from random import randi


def criar_matriz(tamanho: int) -> list[list[int]]:
    """Cria uma matriz a partir do tamanho."""
    matriz = []
    # vai iterar [tamanho = 3] vezes
    for i in range(tamanho):
        # criar uma lista vazia
        lista_temporaria = []
        # vai iterar mais [tamanho = 3] vezes
        for j in range(tamanho):
            # preenchendo a lista com [tamanho = 3] números
            numero = randint(0, 9)
            lista_temporaria.append(numero)
        # guarda a lista temporaria em matriz
        matriz.append(lista_temporaria)
    return matriz


def exibir_matriz(matriz: list[int]):
    for linha in matriz:
        for termo in linha:
            if termo < 10:
                print(str(termo).zfill(2), end=" ")
            else:
                print(termo, end=" ")
        print()


def soma_matriz(matriz1: list[list[int]], matriz2: list[list[int]]) -> list[list[int]]:
    nova_matriz = []
    tamanho = len(matriz1)

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(matriz1[i][j] + matriz2[i][j])
        nova_matriz.append(linha)

    return nova_matriz


tamanho = int(input("Tamanho da matriz: "))

matriz1 = criar_matriz(tamanho)
print("Matriz 1")
exibir_matriz(matriz1)

print("\nMatriz 2")
matriz2 = criar_matriz(tamanho)
exibir_matriz(matriz2)

print("\nMatriz 1 + Matriz 2")
nova_matriz = soma_matriz(matriz1, matriz2)
exibir_matriz(nova_matriz)
