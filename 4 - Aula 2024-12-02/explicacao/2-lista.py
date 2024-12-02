numeros_int = int()
numeros_flt = float()
nome = 'Bruno'
boleanos = True
boleanos = False

#     0  1  2  4
l1 = [1, 2, 3, 4]  # lista de inteiros (homogênea)
l2 = ['bruno', 'silva', 'mateus']  # lista de strings (homogênea)
l3 = [1.2, 3.4, 6.7, 8.9]  # lista de floats (homogênea)
l4 = ['bruno', 28, 1.72]  # lista variada (heterogênea)
#           0        1         2
nomes = ['Bruno', 'Manoel', 'José']
numeros = [1, 2, 3, 4, 3, 2, 1]

tam_nome = len(nomes)
print(f"Tamanho da lista de nomes: {tam_nome}")
# número de posições de uma lista é o seu tamanho - 1

print(f"Lista: {nomes[2]}")

print("\n\n\n\nAdicionando elementos")

# tam: 5
# index: 0 -> 4 (tam - 1)
lista_base = ["manoel", "josé", "mateus", "maria", "joão"]
print("Lista Base:", lista_base)

# remover elemento
lista_base.pop()  # default: remover o último elemento
print("Função pop():", lista_base)

lista_base.pop(1)  # param: index (posição) na lista
print("Função pop(1):", lista_base)

# adicionar
lista_base.append("rafaela")
print("Função append('rafaela'):", lista_base)

# ordenação
numeros = [1, 6, 5, 4, 8, 3, 67, -1, -4, 0]
print("Números desordenados:", numeros)
numeros.sort()
print("Números ordenados (asc):", numeros)
numeros.sort(reverse=True)
print("Números ordenados (desc):", numeros)

nomes = ['maria', 'wesley', 'zaira', 'bruno', 'carlos', 'ana']
print("Nomes desordenados:", nomes)
nomes.sort()
print("Nomes ordenados (a -> z):", nomes)
nomes.sort(reverse=True)
print("Nomes ordenados (z -> a):", nomes)

variados = ['bruno', 1, 45.3]
variados.sort() # não pode, por serem de tipos diferentes

# recapitulando
print("\n\n\n\n\nrecapitulando".upper())
lista = []
print("Lista:", lista)
print("Tamanho:", len(lista))

lista.append("Manoel")
lista.append("João")
print("Lista:", lista)
print("Tamanho:", len(lista))

lista.pop(1)
print("Lista:", lista)
print("Tamanho:", len(lista))

lista.pop()
print("Lista:", lista)
print("Tamanho:", len(lista))
