valores = []

while True:
    numero = int(input("Digite um número: "))
    if numero == -1:
        print("Saindo do laço while ...")
        break
    else:
        valores.append(numero)

print('valores da lista'.capitalize())
contador = 0
while contador < len(valores):
    print(valores[contador])
    contador += 1
