def exibe_pares(lista: list[int]):
    print("\nNúmeros pares:")
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

numeros = [2, 7, 10, 15, 20, 33, 42]

print(f"Lista base: {numeros}")

exibe_pares(numeros)