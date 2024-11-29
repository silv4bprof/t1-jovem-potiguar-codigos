nota = float(input("Digite sua nota: "))

print(f"A sua nota foi: {nota}")

# primeira forma
if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# segunda forma
if nota >= 6:
    print("Aprovado")
elif nota < 6:
    print("Reprovado")