# Escreva um programa que adicione nomes em uma lista até que a palavra 'pare' seja digitado.

nomes = []

while True:
    nome = input("Digite um nome: ")
    nome = nome.lower()
    if nome == 'pare':
        print("Encerrando ...")
        break
    nomes.append(nome)

print(nomes)
