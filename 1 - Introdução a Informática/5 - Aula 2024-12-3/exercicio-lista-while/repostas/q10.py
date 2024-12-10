nomes = []

while True:
    nome = input("Digite um nome: ")
    if nome == 'sair':
        break
    nomes.append(nome)

nomes.sort()  # default: a -> z
posicao = 0

while posicao < len(nomes):
    print(nomes[posicao])
    posicao += 1
