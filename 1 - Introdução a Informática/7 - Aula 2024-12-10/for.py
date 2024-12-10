# exibir a lista
nomes = ['bruno', 'manoel', 'josé', 'marcos', 'antônio']

while True:
    print("\nOpções".upper())
    print("1 - While True:")
    print("2 - While <validacao>")
    print("3 - For + len()")
    print("4 - For in list()")
    print("5 - Sair")

    opcao = int(input("Opção: "))
    """
    while: não sabe quantas iterações (ciclo) irão ocorrer.
    for: quanto sabemos o tamanho do conjunto.
    """
    if opcao == 1:
        print("1 - While True:")
        contador = 0
        while True:
            if contador == len(nomes):
                break
            print(f"{contador}: {nomes[contador]}")
            contador += 1

    elif opcao == 2:
        print("2 - While <validacao>")
        contador = 0
        while contador < len(nomes):
            print(nomes[contador])
            contador += 1
    elif opcao == 3:
        print("3 - For + len()")
        # para cada i no intervalo de 0 -> tam_lista
        for i in range(len(nomes)):  # 0 (incluso) até len(nomes) - 1
            print(nomes[i])

    elif opcao == 4:
        print("4 - For in list()")
        print("Normal")
        for nome in nomes:
            print(nome)

        print("\nEnumerado")
        for indice, nome in enumerate(nomes, start=1):
            print(f'{indice} -> {nome}')
    elif opcao == 5:
        print("Saindo ...")
        break
    else:
        print("Opção inválida!")
