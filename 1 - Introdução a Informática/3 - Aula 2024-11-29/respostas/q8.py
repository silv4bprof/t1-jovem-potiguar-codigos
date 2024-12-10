nota = float(input("Digite sua nota: "))

if nota >= 9:
    print("Excelente")
elif 7 <= nota < 9:
    print("Bom")
elif 5 <= nota < 7:
    print("Regular")
elif (nota < 5):
    print("Reprovado")