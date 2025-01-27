# Questão 9: Aluno com validação de nota
class Aluno:
    def __init__(self, nome: str, nota: int):
        self.__nome = nome
        self.__nota = None
        self.set_nota(nota)

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nota(self) -> int:
        return self.__nota

    def set_nota(self, nota: int):
        try:
            if nota < 0 or nota > 10:
                raise ValueError(
                    f"A nota de {self.get_nome()} deve estar entre 0 e 10."
                )
            self.__nota = nota
        except ValueError as e:
            print(f"Erro: {e}")


aluno1 = Aluno("Manoel", 10)  # da certo
aluno2 = Aluno("Marcos", 11)  # da errado
