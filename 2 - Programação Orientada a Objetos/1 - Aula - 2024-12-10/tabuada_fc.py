# valor default (padrão)

def gerar_tabuada(numero: int = 0):
    for i in range(11):
        print(f"{numero} * {i} = {numero * i}")


def gerar_tabuadas():
    for i in range(1, 11):
        for y in range(1, 11):
            print(f"{i} + {y} = {i + y}")
        print()


gerar_tabuada()
