try:
    with open("notas.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        numeros = [float(linha.strip()) for linha in linhas]
        media = sum(numeros) / len(numeros)
        print(f"A média das notas é {media}")
except FileNotFoundError:
    print("Erro: O arquivo 'notas.txt' não foi encontrado.")
except ValueError:
    print("Erro: O arquivo contém valores não numéricos.")
