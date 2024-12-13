lista = ['carro', 'carro', 'cavalo', 'tela', 'bicicleta', 'bicicleta']
lista_sem_repetidos = []

for palavra in lista:
    if palavra not in lista_sem_repetidos:
        lista_sem_repetidos.append(palavra)

for i in range(len(lista_sem_repetidos)):
    print(f"Posicao[{i}]: {lista_sem_repetidos[i]}")
