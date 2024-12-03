numeros = list(range(1, 11))
numeros_multiplicados = []

contador = 0
while contador < len(numeros):
    multiplicacao = 2 * numeros[contador]
    numeros_multiplicados.append(multiplicacao)
    contador += 1

contador = 0
while contador < len(numeros):
    print(numeros_multiplicados[contador])
    contador += 1

print(numeros)
print(numeros_multiplicados)
