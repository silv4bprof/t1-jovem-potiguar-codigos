class Personagem:
    # Método inicializador (construtor)
    def __init__(self, nome: str, idade: int, profissao: str):
        # características (atributos)
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    # comportamentos (métodos)
    def mudar_profissao(self):
        self.profissao = "Lord"
    
    def ficar_mais_velho(self):
        self.idade += 100

    # métodos do tipo GET (recuperação)
    def apresentar_personagem(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Profissão: {self.profissao}")

    # métodos do tipo SET (atribuição)
    def mudar_nome(self, novo_nome: str):
        self.nome = novo_nome

    # métodos do tipo setters
    # métodos do tipo getters
            

# instância de personagem
dracula = Personagem('Drácula', 300, 'Vampiro')

print(dracula.nome)

exit(0)
dracula.apresentar_personagem()

print("\nFicando mais velho")
# chamei o comportamento
dracula.ficar_mais_velho()

print("\nMudando de profissão")
# chamei o comportamento
dracula.mudar_profissao()

print("\nMudando nome para Vladmir")
dracula.mudar_nome(novo_nome='Vladmir')

print("\nDados do personagem")
# chamei o comportamento
dracula.apresentar_personagem()