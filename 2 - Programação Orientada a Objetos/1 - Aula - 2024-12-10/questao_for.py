numeros = []
for i in range(5):  # 0 -> 4
    numero = int(input("Número: "))
    numeros.append(numero)

# 100, 23, 50, 700
maior = numeros[0]
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        if numeros[i] > maior:
            maior = numeros[i]
        
print("Maior número par:", maior)

menor = numeros[0]
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        if numeros[i] < menor:
            menor = numeros[i]

print("Menor número ímpar:", menor)