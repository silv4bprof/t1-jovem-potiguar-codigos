preco = float(input("Preço do produto: "))
desconto = int(input("Desconto (%): "))

# valor subtraído o desconto 
valor_desconto = (preco * desconto) / 100
valor_descontado = preco - valor_desconto

print("O valor aplicado o desconto é:", valor_descontado)