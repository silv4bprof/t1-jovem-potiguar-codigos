numeros = []

while True:
    numero = int(input("Digite um número para inserir: "))
    if numero != 0:
        numeros.append(numero)
    else:
        print("Encerrando ...")
        break

contador = 0
soma = 0
while contador < len(numeros):
    soma = soma + numeros[contador]
    contador += 1

print(f"Soma dos números digitados: {soma}")
