class Animal:
    def __init__(self, nome="Animal"):
        self.__nome = nome

    def fazer_som(self):
        print("Som Genérico")


class Cachorro:
    def fazer_som(self):
        super().fazer_som()
        print("Au Au!")


cachorro = Cachorro()
cachorro.fazer_som()
