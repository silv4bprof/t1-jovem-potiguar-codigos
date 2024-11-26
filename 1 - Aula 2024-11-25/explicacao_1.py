# Variáveis
# tipo texto
nome = "Roberta Santos" # string (cadeira de caracteres)
letra = 'b' # char (um caracter)

# numérico
inteiro = 1 # int (inteiro)
decimal = 1.4 # float (flutuante)
idade = 28

# booleanos
verdadeiro = True # bool true
falso = False # bool false

# listas homogêneas
lista_numeros = [1, 2, 3, 4, 5] # lista de inteiros
lista_numeros = [1.1, 2.2, 3.1] # lista de flutuantes

# lista heterogêneas
dados_pessoais = ["Bruno", 28, 1.72, 'M']
dados_pessoais_2 = ("Bruno", 28, 1.72, 'M')

nome = "Bruno"
nomeCompleto = "Bruno Borges da Silva" # camelCase
idade = 28
altura_m = 1.72 # snake_case
altura_cm = 172 # snake_case

# Exibição de Variáveis (dados)
print("Meu nome é", nome)
print("Meu nome completo:", nomeCompleto)
print("Eu tenho", idade, "anos de idade")
print("Minha altura (metros) é:", altura_m, "M")
print("Minha altura (centímetros) é:", altura_cm, "Cm")

# Exibição de Variáveis (tipos)
print()
print("Tipos de variáveis")
print()
print("Variável 'nome' é do tipo:", type(nome))
print("Variável 'idade' é do tipo:", type(idade))
print("Variável 'verdadeiro' é do tipo:", type(verdadeiro))
print("Variável 'lista_numeros' é do tipo:", type(lista_numeros))
print("Variável 'dados_pessoais_2' é do tipo:", type(dados_pessoais_2))
print()