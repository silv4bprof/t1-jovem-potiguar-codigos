temperaturas = [30, 25, 28, 35, 22, 27]

qtd_temperaturas = len(temperaturas)
soma, contador = 0, 0

while contador < qtd_temperaturas:
    soma += temperaturas[contador]
    contador += 1

media = soma/qtd_temperaturas
print(f"Média das temperatudas: {media}")
