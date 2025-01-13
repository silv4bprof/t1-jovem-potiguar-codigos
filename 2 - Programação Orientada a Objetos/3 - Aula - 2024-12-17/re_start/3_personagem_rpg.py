class Personagem:
    def __init__(self, nome, idade, vida):
        self.nome = nome # público
        self.idade = idade
        self.vida = vida

    def se_apresente(self):
        print(
            f"\nMeu nome é {self.nome}\nEu tenho {self.idade} anos de idade.\nVida atual: {self.vida}"
        )


p1 = Personagem("Mario", 40, 100)
p2 = Personagem("Luigi", 40, 100)

p1.se_apresente()
p2.se_apresente()

p1.idade = p1.idade + 1
p1.vida = p1.vida - 10

p1.se_apresente()
p2.se_apresente()
