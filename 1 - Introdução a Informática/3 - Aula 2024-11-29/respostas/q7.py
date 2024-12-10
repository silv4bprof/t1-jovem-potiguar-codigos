num1 = int(input("1º Número: "))
num2 = int(input("2º Número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Operação: "))

if operacao == 1:
    print("Soma")
    print(f"Resultado: {num1 + num2}")
elif operacao == 2:
    print("Subtração")
    print(f"Resultado: {num1 - num2}")
elif operacao == 3:
    print("Multiplicação")
    print(f"Resultado: {num1 * num2}")
elif operacao == 4:
    print("Divisão")
    if num2 == 0:
        print("Indefinido.")
    else:
        print(f"Resultado: {num1 / num2}")
else:
    print("Operação inválida.")
