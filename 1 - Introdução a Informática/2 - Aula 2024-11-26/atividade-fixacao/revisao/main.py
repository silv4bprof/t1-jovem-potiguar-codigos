nome = str("Bruno Silva") # string - str
sexo = 'M' # caracter - char
idade = 28 # integer - int
altura = 1.72 # floating - float
fato = True # boleano - bool (boolean)
fato = False # boleano - bool (boolean)
numeros = [1,2,3,5,6] # lista (homo)
palavras = ['bruno', 'ana', 'maria'] # lista (homo)
dados_pessoas = ['bruno',28,1.72] # lista (hete)

# exibindo nada - pulando linha
print()

# exibindo um valor
print("Valor estático")
print(28)
print(2.5)
print(nome)

# exibindo valores
print(nome,idade,'palavra qualquer',2.5)

# calculos
n1 = 25 + 5
print("Resultado:", n1)

fato = 25 == 25
print("Resultado:", fato)

fato = 25 != 25
print("Resultado:", fato)

fato = 25 >= 5
print("Resultado:", fato)

fato = 20 > 6
print("Resultado:", fato)

# receber dados

# nome = input("Digite seu nome: ")
# print("O nome digitado foi", nome)

# tipos

print("Tipo de dado de idade:", type(idade))
print("Tipo de dado de fato:", type(fato))
print("Tipo de dado de numeros:", type(numeros))