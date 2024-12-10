valores = []

while True:
    numero = int(input("Número: "))
    if numero == -1:
        print("Encerrando ...")
        break
    valores.append(numero)

print(valores)