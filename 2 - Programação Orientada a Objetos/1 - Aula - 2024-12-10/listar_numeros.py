numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Numeros pares\n")
for num in numeros:
    if num % 2 == 0:
        print(f"Número {num}")

print("Numeros ímpares\n")
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        print(f"Número {numeros[i]}")