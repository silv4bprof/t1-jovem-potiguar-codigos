frutas = ['maçã', 'banana', 'laranja', 'uva']
tam_frutas = len(frutas)
contador = 0

while contador < tam_frutas:
    print(f"Removendo {frutas[0]} da lista.")
    frutas.pop(0)
    contador += 1
