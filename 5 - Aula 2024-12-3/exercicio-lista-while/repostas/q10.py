nomes = []

while True:
    nome = input("Digite um nome: ")
    if nome.lower() == 'sair':
        print("Saindo ...")
        break
    else:
        nomes.append(nome)

contador = 0
print('Exibindo os nomes cadastrados:\n')
while contador < len(nomes):
    print(nomes[contador])
    contador += 1
