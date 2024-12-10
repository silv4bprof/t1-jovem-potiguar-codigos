pares = []
numero_vez = 0

while numero_vez <= 20:
    resto = numero_vez % 2
    if resto == 0:
        pares.append(numero_vez)
    numero_vez = numero_vez + 1

print(pares)