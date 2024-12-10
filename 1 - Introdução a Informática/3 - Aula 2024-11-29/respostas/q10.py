# import random
# numero_sorteado = random.randint(0, 100)

from random import randint
numero_sorteado = randint(0, 100)

# print(f"Sorteado: {numero_sorteado}")

numero = int(input("Tente acertar o número secreto: "))

if numero < numero_sorteado:
    print("Muito baixo")
elif numero > numero_sorteado:
    print("Muito alto")
else:
    print("Você acertou")