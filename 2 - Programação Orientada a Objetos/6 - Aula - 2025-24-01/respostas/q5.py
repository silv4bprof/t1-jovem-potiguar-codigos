# Questão 5: Login com validação de senha
class Login:
    def __init__(self, usuario: str, senha: str = None):
        self.__usuario = usuario
        self.__senha = senha

    def get_usuario(self) -> str:
        return self.__usuario

    def set_usuario(self, usuario: str):
        self.__usuario = usuario

    def get_senha(self) -> str:
        return self.__senha

    def set_senha(self, senha: str):
        try:
            if len(senha) < 6:
                raise Exception("A senha deve ter pelo menos 6 caracteres.")
            self.__senha = senha
        except Exception as e:
            print(f"Erro: {e}")
        else:
            print("Senha salva com sucesso!")
        finally:
            print("Finalizando tratamento de senha.")


user = Login("@silv4b")
senha = input(f"Senha de {user.get_usuario()}: ")
user.set_senha(senha)
