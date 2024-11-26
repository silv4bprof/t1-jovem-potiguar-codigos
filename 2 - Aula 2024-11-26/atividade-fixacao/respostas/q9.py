peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# 1ª forma
imc = peso / (altura ** 2) # altura²

# 2ª forma
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc}")
