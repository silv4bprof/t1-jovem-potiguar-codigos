numeros = []
# preenche a lista
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

print(numeros)
# somatório
posicao = 0
soma = 0
while posicao < len(numeros):
    soma = soma + numeros[posicao]
    posicao = posicao + 1
print(soma)

# percorrendo a lista
posicao = 0
while posicao < len(numeros):
    print(f"Valor: {numeros[posicao]}")
    posicao = posicao + 1