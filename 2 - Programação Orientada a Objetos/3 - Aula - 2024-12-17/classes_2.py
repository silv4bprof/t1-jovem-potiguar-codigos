# receita de como criar um personagem
# palavra reservada: class
# nome da classe: Personagem (capitalizado)
class Personagem:
    # A class Personagem representa as características de uma identidade personagem em um jogo
    # Inicializador (construtor)
    def __init__(self):
        # Inicializa as propriedades de um personagem
        self.nome = 'Alucard'
        self.idade = 120
        self.profissao = 'Matador de vampiro'


alucard = Personagem()
print(f"""
Nome: {alucard.nome}
Idade: {alucard.idade}
Profissão: {alucard.profissao}
""")

dracula = Personagem()
# dracula.nome = 'Dracula'
# dracula.idade = 300
# dracula.profissao = 'Vampiro'

print(f"""
Nome: {dracula.nome}
Idade: {dracula.idade}
Profissão: {dracula.profissao}
""")