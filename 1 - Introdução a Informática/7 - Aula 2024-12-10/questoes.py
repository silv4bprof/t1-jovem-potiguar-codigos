nomes = ['bruno', 'manoel', 'josé', 'marcos', 'antônio']
tamanho = len(nomes)

# primeira forma
print("Exibindo nomes 1ª Forma.\n")
for posicao in range(tamanho):
    print(f"nomes[{posicao}]: {nomes[posicao]}")

print("\nExibindo nomes 2ª Forma.\n")
print("Padrão:\n")
for nome in nomes:
    print(nome)

print("\nEnumerada:\n")
for indice, nome in enumerate(nomes, start=0):
    print(f"nomes[{indice}]: {nome}")