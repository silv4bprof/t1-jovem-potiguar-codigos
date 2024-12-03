pares = []

contador = 0
ate = 20

while contador < ate+1:
    if contador % 2 == 0:
        pares.append(contador)
    contador += 1

print('valores da lista'.capitalize())
contador = 0
while contador < len(pares):
    print(pares[contador])
    contador += 1
