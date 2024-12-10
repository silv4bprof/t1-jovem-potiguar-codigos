def menu():
    """
    docstring
    Nome: Menu()
    Função: Exibir menu.
    """
    print("""
\nOpções Disponíveis
          
1 - Preencher uma lista (append)
2 - Exibir lista preenchida (for)
3 - Somar elementos de uma lista de inteiros (for)
4 - Excluir o elemento de uma lista (pop)
5 - Exibir lista ordenada (desc ou asc)
    """)


def preencher_lista(qtd_itens):
    """
    Retorna uma lista preenchida pelo usuário.
    """
    lista = []
    for i in range(qtd_itens):
        item = int(input(f"{i+1}º número: "))
        lista.append(item)
    return lista


def exibir_lista(lista, exibir_pos=False):
    print("Exibindo Lista:\n")
    if exibir_pos == False:
        for elemento in lista:
            print(elemento, end=' ')
    else:
        for indice, num in enumerate(lista, start=0):
            print(f"Posicao[{indice}]: {num}")


def somar_elementos(lista):
    soma = 0
    for elemento in lista:
        soma = soma + elemento
    return soma


def remover_elemento(lista: list, posicao: int):
    lista.pop(posicao)
    return lista


def exibir_ordena_lista(lista: list):
    print('1 - Crescente')
    print('2 - Decrescente')
    opcao = int(input("Opção: "))
    if opcao == 1:
        lista.sort()
        exibir_lista(lista)
    elif opcao == 2:
        lista.sort(reverse=True)
        exibir_lista(lista)
    else:
        print("Erro ...")
