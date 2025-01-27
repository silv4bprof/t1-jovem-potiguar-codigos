class NumeroNegativo(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem


try:
    num1 = int(input("Numero: "))
    num2 = int(input("Numero: "))

    if (num1 < 0) or (num2 < 0):
        raise NumeroNegativo("Número não pode ser negativo.")

    resultado = num1 / num2
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except ValueError as e:
    print(f"Erro: {e}")
except NumeroNegativo as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
