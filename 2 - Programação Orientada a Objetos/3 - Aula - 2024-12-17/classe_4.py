class Animal:
    """
    Classe Animal:
    Atributos:
    - cor: cor do animal
    - nome: nome do animal
    - tipo: tipo do animal (aquático ou terrestre)
    """
    def __init__(self, nome, cor, tipo):
        # atributos privados
        self.__nome = nome
        self.__cor = cor
        self.__tipo = tipo
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_cor(self, cor):
        self.__cor = cor

    def set_tipo(self, tipo):
        self.__tipo = tipo

    # Getters
    def get_nome(self):
        print(f"Nome: {self.__nome}")
    
    def get_cor(self):
        print(f"Cor: {self.__cor}")

    def get_tipo(self):
        print(f"Tipo: {self.__tipo}")

    # Método especial __str__
    def __str__(self):
        return f"{self.__nome} - {self.__cor} - {self.__tipo}"


# Instância da classe (Animal)
cachorro = Animal('Bob', 'Caramelo', 'Terrestre')
print("\nExibindo dados do Animal")
cachorro.get_nome()
cachorro.get_cor()
cachorro.get_tipo()

print("\nAlterando dados do Animal ...")
cachorro.set_nome('Rex')
cachorro.set_cor('Preto')

print("\nExibindo NOVOS dados do Animal")
cachorro.get_nome()
cachorro.get_cor()
cachorro.get_tipo()

# Outra instância da classe (Animal)
gato = Animal('Garfield', 'Amarelo Alaranjado', 'Terrestre')
print("\nExibindo dados do Gato usando __str__")
print(str(gato))
