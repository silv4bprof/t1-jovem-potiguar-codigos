# escreva um programa que calcule uma das operações básicas (soma, subtração, multiplicação e divisão), após o calculo, o programa deve perguntar se o usuário quer fazer outra operação, se 'sim' continue, se 'nao', encerre o programa.

while True:
    print("Calculadora Simples")
    continuar = input("Deseja realizar uma operação ('sim' ou 'nao'): ")
    
    if continuar == 'nao':
        print("Encerrando o programa ...")
        break
    elif continuar == 'sim':
        num1 = int(input("Digite o 1º termo: "))
        num2 = int(input("Digite o 2º termo: "))

        print("Operações Disponíveis")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = int(input("Escolha a operação: "))

        if opcao == 1:
            print(f"Resultado da soma: {num1 + num2}")
        elif opcao == 2:
            print(f"Resultado da subtração: {num1 - num2}")
        elif opcao == 3:
            print(f"Resultado da multiplicação: {num1 * num2}")
        elif opcao == 4:
            if num2 == 0:
                print("Operação inválida para divisão")
            else:
                print(f"Resultado da divisão: {num1 / num2}")
        else:
            print("Opção inválida ...")
    else:
        print("Opção inválida ...")
