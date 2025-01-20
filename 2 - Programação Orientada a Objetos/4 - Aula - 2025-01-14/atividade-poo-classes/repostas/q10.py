class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro_ponto):
        if isinstance(outro_ponto, Ponto):
            # somar os pontos de x dos pontos e soma os pontos de y dos pontos
            # retornando um novo Ponto, onde o x e y são as somas respectivamente
            return Ponto(self.x + outro_ponto.x, self.y + outro_ponto.y)
        raise TypeError("A soma só pode ser feita entre dois objetos do tipo Ponto.")

    def __repr__(self):
        return f"({self.x}, {self.y})"


# Exemplo de uso
ponto1 = Ponto(1, 2)
ponto2 = Ponto(3, 4)
resultado = ponto1 + ponto2

print(resultado)  # Saída: "(4, 6)"
