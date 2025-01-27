class IdadeNegativa(Exception):
    def __init__(self, exception):
        super().__init__(exception)
        self.exception = exception


try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        raise IdadeNegativa("Idade não pode ser negativa.")
except ValueError:
    print("Erro: Você não digitou um número válido.")
except IdadeNegativa as e:
    print(f"Erro: {e}")
else:
    print(f"Sua idade é {idade} anos.")
