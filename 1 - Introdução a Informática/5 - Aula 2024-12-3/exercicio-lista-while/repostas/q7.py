numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobrados = []

tamanho_lista = len(numeros)
posicao = 0

while posicao < tamanho_lista:
    multiplicacao = 2 * numeros[posicao]
    dobrados.append(multiplicacao)
    posicao = posicao + 1


posicao = 0
tamanho_lista = len(dobrados)
while posicao < tamanho_lista:
    print(f"Valor: {dobrados[posicao]}")
    posicao += 1
