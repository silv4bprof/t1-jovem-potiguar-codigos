n1 = 3 # int
n2 = 5 # int

n1 = int(input("Digite um número (n1): "))
n2 = int(input("Digite um número (n2): "))

print("Calculadora [+, -, *, /]")
print()

print("Números:", n1, "e", n2)
print("Operações básicas")

n3 = n1 + n2
print("Resultado (+):", n3) # 50

n4 = n1 - n2
print("Resultado (-):", n4) # 40

n5 = n1 * n2
print("Resultado (*):", n5) # 225

n6 = n1 / n2
print("Resultado (/):", n6) # 9.0

print()
print("Operações Complexas")

n7 = (n1 + n2) * n2
print("(",n1,"+",n2,")","*",n2,"=",n7)
print(f"({n1} + {n2}) * {n2} = {n7}")