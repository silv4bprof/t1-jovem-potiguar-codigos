palavras = ['treta', 'confusão', 'tiro', 'porrada', 'bomba']
tamanho = len(palavras)
posicao = 0
qtd_palavras_maior_cinco = 0

while posicao < tamanho:
    if len(palavras[posicao]) > 5:
        # qtd_palavras_maior_cinco = qtd_palavras_maior_cinco + 1
        qtd_palavras_maior_cinco += 1
    posicao = posicao + 1

print(f"{qtd_palavras_maior_cinco} palavras tem mais de 5 letras.")