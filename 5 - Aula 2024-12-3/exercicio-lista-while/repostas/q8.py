palavras = ['barraco', 'treta', 'confusão', 'briga']

contador = 0

while contador < len(palavras):
    palavra = palavras[contador]
    if len(palavra) > 5:
        print(f"{palavra} tem mais de 5 letras".capitalize())
    contador += 1
