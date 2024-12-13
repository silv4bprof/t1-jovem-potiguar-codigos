qtd_alunos = int(input("Quantidade de alunos: "))
notas = []

for i in range(qtd_alunos):
    nota = int(input("Nota do aluno: "))
    notas.append(nota)

contador = 0
for nota in notas:
    if nota >= 60:
        contador += 1

print(f"{contador} alunos estão na média.")

contador = 0
for nota in notas:
    if nota < 60:
        contador += 1

print(f"{contador} alunos NÃO estão na média.")
