# Escreva um programa em que o usuário digite números de forma indeterminada, até que o número -1 seja digitado.

print("""
Opção de While
1 - while <expressao>:
2 - while True: break
""")

opcao = int(input("Tipo de while: "))

if opcao == 1:
    # while <expressao>:
    numero = int(input("Digite um número (-1 para sair): "))

    while numero != -1:  # start do while
        print(f"Número digitado: {numero}")
        numero = int(input("Digite um número (-1 para sair): "))
        # end do while (volta pra o start)

    print("Saiu do laço|estrutura de repetição.")
elif opcao == 2:
    # while True: break
    while True:
        numero = int(input("Digite um número (-1 para sair): "))
        if numero == -1: # condição de parada
            print("Saindo ...")
            break
        print(f"Número digitado: {numero}")
    print("Saiu do laço|estrutura de repetição.")

    # fim do laço (voltar pra o início)
