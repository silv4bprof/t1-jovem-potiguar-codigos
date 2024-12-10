from funcoes import menu
from funcoes import preencher_lista
from funcoes import exibir_lista
from funcoes import somar_elementos
from funcoes import remover_elemento
from funcoes import exibir_ordena_lista

lista_preenchida = []

while True:
    menu()
    opcao = int(input("Opção: "))

    if opcao == 1:
        lista_preenchida = preencher_lista(5)
    elif opcao == 2:
        exibir_lista(lista_preenchida)
    elif opcao == 3:
        soma_res = somar_elementos(lista_preenchida)
        print(f"Soma total: {soma_res}")
    elif opcao == 4:
        exibir_lista(lista_preenchida, True)
        posicao = int(input("Digite a posição P/ remoção: "))
        lista_preenchida = remover_elemento(lista_preenchida, posicao)
        exibir_lista(lista_preenchida)
    elif opcao == 5:
        exibir_ordena_lista(lista_preenchida)
    else:
        print("Saindo ...")
        break
