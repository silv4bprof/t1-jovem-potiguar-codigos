# Questão 3: Usuario com validação de email
class EmailInvalido(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem


class Usuario:
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = None
        self.set_email(email)

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        try:
            if ("@" not in email) or (".com" not in email):
                raise EmailInvalido("Email inválido para as especificações!")
            self.__email = email
        except EmailInvalido as e:
            print(f"Erro de Email: {e}")
        except ValueError as e:
            print(f"Erro de Valor: {e}")


email_valido = "brunno.linkin@gmail.com"
email_invalido = "brunno.linkin-gmail,com"

usuario = Usuario("Manoel Marcos", email_valido)
usuario.set_email(email_invalido)
