numeros = [10, 20, 30, 40, 120, 150]
tamanho_lista = len(numeros)  # 8
contador = 0

print(f"Lista: {numeros}")
print(f"Tamanho da lista: {tamanho_lista}")
print(f"Índices de 0 -> {tamanho_lista-1}\n")

while contador < tamanho_lista:
    print(f"Quando o 'contador' for {contador}")
    print(f"Valor da posição {contador}: {numeros[contador]}\n")
    contador = contador + 1
