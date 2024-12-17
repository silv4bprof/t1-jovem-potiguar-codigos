def imprimir_sequencia():
    for i in range(1, 11):
        print(f"Número: {i}")

def imprimir_sequencia_atr(inicio: int, fim: int):
    fim = fim + 1
    for i in range(inicio, fim):
        print(f"Número: {i}")

print("Primeira função: imprimir_sequencia()")
imprimir_sequencia()

print("\nSegunda função: imprimir_sequencia_atr(inicio, fim)")
imprimir_sequencia_atr(0, 100)