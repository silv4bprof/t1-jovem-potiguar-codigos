# casting

"""
Tipos base:

str()   -> string: cadeia de caracteres.
int()   -> integer: números inteiros (+ ou -).
float() -> floating: números fluturantes (+ ou -).

"""

n1 = 9 # int
print("Número:", n1)
print("Tipo:", type(n1))
print()

n2 = float(n1) # float
print("Número:", n2)
print("Tipo:", type(n2))
print()

# n3 = input("Digite um número: ") # str()
# print("Número:", n3)
# print("Tipo:", type(n3)) # str()

# n4 = int(n3) # att ou upd
# print("Tipo:", type(n4)) # int()
# print()

n3 = int(input("Digite um número inteiro: "))
print("O número digitado foi:", n3)
print("E o seu tipo é:", type(n3))

n4 = float(input("Digite um número decimal: "))
print("O número digitado foi:", n4)
print("E o seu tipo é:", type(n4))