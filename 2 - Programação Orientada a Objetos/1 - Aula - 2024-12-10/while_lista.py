# conjunto de dados lista | array
lista = ['bruno', 'manoel', 'josefina']
print(lista)
print(f"Tamanho da lista: {len(lista)}")

print("Adicionando nomes na lista (append)")
lista.append('wemylly')
lista.append('eloa')
lista.append('brenda')
lista.append('mariana')

print(f"Tamanho da lista atualizado: {len(lista)}")

print(lista)
tamanho_lista = len(lista)
for i in range(tamanho_lista):
    print(f"Valor na {i} da lista: {lista[i]}")

print("Removendo nomes na lista (pop)")
"""
lista.pop() -> remove sempre o ultimo elemento da lista
lista.pop(2) -> pode receber um numero como parâmetro. sendo esse número, a posição na lista onde o dado vai ser removido
"""

print(lista)
print("Removendo o ultimo nome")
lista.pop()
print(lista)
print("Removendo nome da posição 0")
lista.pop(0)
print(lista)

