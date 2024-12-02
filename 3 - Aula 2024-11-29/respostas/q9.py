lado1 = int(input("Digite 1º o lado do triângulo: "))
lado2 = int(input("Digite 2º o lado do triângulo: "))
lado3 = int(input("Digite 3º o lado do triângulo: "))

if (lado1 == lado2) and (lado2 == lado3) and (lado3 == lado1):
    print("Equilátero")
elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
    print("Isósceles")
elif (lado1 != lado2) and (lado2 != lado3) and (lado3 != lado1):
    print("Escaleno")
