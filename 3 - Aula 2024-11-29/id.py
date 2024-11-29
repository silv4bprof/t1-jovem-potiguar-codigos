# recebo a idade do usuário
idade = int(input("Digite sua idade: "))

# exibo a idade do usuário
print("Idade:", idade)

# (se idade for maior ou igual a 18)
if idade >= 18:  # verifico se é maior
    print("Você é maior de idade.")
# (se não, verifique se idade é menor que 18)
elif idade < 18:  # verifico se é menor
    print("Você é menor de idade.")
else:
    ...


numero = int(input("Digite um número: "))
print(f"Número digitado: {numero}")


# intervalo de  1 -> 10: 20
# 0 excludente

numero = int(input("Digite um número: "))
print(f"Número digitado: {numero}")

if (numero >= 1) and (numero <= 10):
    print("Número no intervalo de 1 e 10")
elif (numero >= 11) and (numero <= 20):
    print("Número no intervalo de 11 e 20")
else:
    print("Número em nenhum intervalo.")
