def multiplica(numero: int):
    print(f"Tabela de {numero}")
    for i in range(1, 11):
        print(f"{numero} * {i} = {i * numero}")

numero = int(input("Tabela de: "))

multiplica(numero)
