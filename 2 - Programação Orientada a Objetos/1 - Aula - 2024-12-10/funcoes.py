def meu_print(frase):
    print(frase)


def soma(n1, n2):
    res = n1 + n2
    return res


def subtracao(n1, n2):
    res = n1 - n2
    return res


def multiplicacao(n1, n2):
    res = n1 * n2
    return res


def divisao(n1, n2):
    if n2 == 0:
        res = "Indefinido"
    else:
        res = n1 / n2
    return res
