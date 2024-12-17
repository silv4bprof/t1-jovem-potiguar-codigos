def soma(lista: list):
    soma = 0
    for numero in lista:
        soma = soma + numero

    print(f"Resultado da soma: {soma}")

numeros = [5, 8, 12, 20, 3]

soma(numeros)