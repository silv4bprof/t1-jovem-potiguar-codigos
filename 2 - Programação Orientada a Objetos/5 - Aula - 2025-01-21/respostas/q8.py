import math

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    produto = num1 * num2
    raiz = math.sqrt(produto)
    print(f"A raiz quadrada do produto é {raiz}")
except ValueError:
    print("Erro: Entrada inválida ou resultado negativo para a raiz.")
