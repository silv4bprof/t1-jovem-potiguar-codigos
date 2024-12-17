class Pessoa:
    """
    Atributos:
    - nome(str): nome da pessoa (privado).
    """
    def __init__(self, nome: str, email: str = "default@gmail.com"):
        self.__nome = nome
        self.__email = email

    
    # Setter
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email

    # Getter
    def get_nome(self):
        print(f"Nome: {self.__nome}")

    def get_email(self):
        print(f"Email: {self.__email}")

    # Método especial __str__
    def __str__(self):
        return f"{self.__nome}\n{self.__email}"


# Instância da classe (Animal)
uma_pessoa = Pessoa('José')
print(str(uma_pessoa))

print()
outra_pessoa = Pessoa('Bruno', 'brunno.linkin@gmail.com')
print(str(outra_pessoa))