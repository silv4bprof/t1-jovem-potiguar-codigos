temperaturas = [30, 25, 28, 35, 22, 27, 100]

posicao = 0
soma = 0

print(f"Lista: {temperaturas}")
while posicao < len(temperaturas):
    soma = soma + temperaturas[posicao]
    posicao += 1

print(f"Soma das temperaturas: {soma}")

media = soma / len(temperaturas)
print(f"Média das temperaturas: {media:.2f}")
