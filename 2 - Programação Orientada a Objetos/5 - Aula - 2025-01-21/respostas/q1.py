try:
    numero = int(input("Digite um número: "))
    print(f"O dobro do número é {numero * 2}")
except ValueError:
    print("Erro: Você não digitou um número válido.")
