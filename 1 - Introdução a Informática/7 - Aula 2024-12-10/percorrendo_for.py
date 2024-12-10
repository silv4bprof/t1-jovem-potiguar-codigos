dados_pessoais = ['Bruno Silva', 28, 1.72, 28.3]

for i in range(len(dados_pessoais)):
    print(dados_pessoais[i])

for dado in dados_pessoais:
    print(dado)

for indice, dado in enumerate(dados_pessoais, start=0):
    print(f"dados_pessoais[{indice}]: {dado}")

print("\nTabuada de algum número")
numero = int(input("Digite um número p/ multiplicar: "))

for i in range(0, 11):
    print(f"{i} * {numero} = {i * numero}")

numero = int(input("Digite um número p/ multiplicar: "))
inicio = int(input("De: "))
final = int(input("Até: "))

for i in range(inicio, final + 1):
    print(f"{i} * {numero} = {i * numero}")


print("Contando letras de nome")
seu_nome = input("Digite seu nome: ")

for letra in seu_nome:  # bruno -> 5
    print(letra)
