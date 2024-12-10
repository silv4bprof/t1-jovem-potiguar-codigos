frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']

tamanho = len(frutas)
posicao = 0

print(f"Lista base: {frutas}")
while posicao < tamanho:
    print(f"Removendo {frutas[0]}")
    frutas.pop(0)
    print(f"Lista atualizada: {frutas}")
    posicao += 1  # contador = contador + 1
