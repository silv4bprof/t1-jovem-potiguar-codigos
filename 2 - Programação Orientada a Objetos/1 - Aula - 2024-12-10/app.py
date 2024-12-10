from funcoes import soma, subtracao, multiplicacao, divisao
from funcoes import meu_print

meu_print(
    """
Escolha sua operação:
1 - +
2 - -
3 - *
4 - /
5 - (*) + 10
"""
)

opcao = int(input("Opção: "))

n1 = int(input("N1: "))
n2 = int(input("N2: "))

if opcao == 1:
    print(f"Soma: {soma(n1, n2)}")
elif opcao == 2:
    print(f"Subtração: {subtracao(n1, n2)}")
elif opcao == 3:
    print(f"Multiplicação: {multiplicacao(n1, n2)}")
elif opcao == 4:
    print(f"Divisão: {divisao(n1, n2)}")
elif opcao == 5:
    mult_res = multiplicacao(n1, n2)
    soma_res = soma(mult_res, 10)
    meu_print(f"Resultado: {soma_res}")
