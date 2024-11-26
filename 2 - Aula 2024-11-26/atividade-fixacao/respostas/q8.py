numero = int(input("Digite um número: "))

"""
div = numero / 2
print(f"Resultado da divisão: {div}")

res = numero % 2
print(f"Resto da divisão: {res}")
"""

resto = numero % 2
if resto == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

"""
if condicao -> verdadeira:
    codigo
"""