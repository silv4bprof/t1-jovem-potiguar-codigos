class Aluno:
    def __init__(self, nome: str, email: str, notas: list[float] = []):
        self.__nome = nome
        self.__email = email
        self.__notas = notas
    
    # getters
    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_notas(self) -> list[float]:
        return self.__notas

    # setters
    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_email(self, email: str):
        self.__email = email

    def set_nota(self, nota: float):
        # validação: verificar se já tem 4 notas
        self.__notas.append(nota)

    # sobreposição
    def __str__(self):
        return f"Nome: {self.__nome}\nEmail: {self.__email}\nNotas: {self.__notas}\nMédia: {self.calcular_media()}\n"
    
    # métodos "normais"
    def calcular_media(self) -> float | str:
        soma = sum(self.__notas)
        tam = len(self.__notas)
        if tam == 0:
            return "Não foi possivel calcular."
        return soma/tam


aluno1 = Aluno('Manoel', 'manoel@gmail.com')
aluno2 = Aluno('Maria', 'maria@gmail.com', [10, 10, 10, 10])
aluno3 = Aluno('Jorge', 'jorge@gmail.com', [8, 10, 5, 6])
aluno4 = Aluno('João', 'joao@gmail.com')

alunos = []
alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)

for aluno in alunos:
    print(str(aluno))