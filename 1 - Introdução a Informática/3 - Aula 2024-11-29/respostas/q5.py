imc = float(input("Digite seu IMC: "))

if (imc < 18.5):
    print("Abaixo do peso")
# elif (18.5 <= imc < 25):
elif (imc >= 18.5) and (imc <= 25):
    print("Peso normal")
elif (imc >= 25):
    print("Acima do peso")
