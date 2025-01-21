print("=== Digite seu nome e idade ===")

try:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
except ValueError as e:
    print("Idade deve ser em números.")
    print(f"Error: {e}")
finally:
    print("Passo 1: Finalizado.")

print("\n=== Divisão de Números ===")

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))

# try:
#     resultado = num1 / num2
# except:
#     print("Não dividirás por 0.")

try:
    resultado = num1 / num2
    print(resultado)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Passo 2: Finalizado.")
    
numero_aleatorio = 78
num = int(input("Acerto o número aleatório: "))

if num == numero_aleatorio:
    print("PARABÉNS 🚀")
else:
    raise Exception('VOCÊ ERRO, OTÁRO!')
