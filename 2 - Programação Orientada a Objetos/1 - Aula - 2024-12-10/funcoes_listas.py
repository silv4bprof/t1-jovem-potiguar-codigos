lista = ['Bruno', 'Maria', 'José', 'Daniel', 'Anna']
numeros = [1, 2, 3, 45, 63, 56, 78, 67, 86, 786,]
flutuantes = [1.3, 2.4, 5.3, 6.6, 5.8, 3.9, 34.3]


def exibe_lista(lista: list):
    print(f"Exibindo a lista")
    for indice, nome in enumerate(lista, start=1):
        print(f"{indice}: {nome}")


exibe_lista(lista)
exibe_lista(numeros)
exibe_lista(flutuantes)
