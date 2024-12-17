def calcula_media(medias: list[float]) -> float:
    soma = 0
    print("Notas")
    for nota in medias:
        print(f"Nota: {nota}")
        soma = soma + nota
    media = soma/qtd_notas
    return media
    

notas = [7.5, 8.0, 6.5, 9.0, 7.0]
qtd_notas = len(notas) # tamanho

media = calcula_media(notas)

print(f"Média das notas: {media}")