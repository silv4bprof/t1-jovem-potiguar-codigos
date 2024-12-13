# gerador de tabuada
num = int(input("Tabuada de: "))
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

# range: limite inferior (includente)
# range: limite superior (excludente)
for i in range(inicio, fim + 1):
    print(f"{num} x {i} = {num * i}")
