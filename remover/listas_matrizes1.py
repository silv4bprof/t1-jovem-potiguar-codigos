lista = []
lista_maior = []

for i in range(0, 5):
    for j in range(0, 5):
        lista.append(j)
    lista_maior.append(lista)

for elemento in lista_maior:
    print(elemento)
