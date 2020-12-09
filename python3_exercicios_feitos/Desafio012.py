#FUPQ leia o preço de um produto e mostre seu novo preço com 5% de desconto
prod = float(input('Preço do produto: R$'))
desconto = prod - (prod*0.05)
print(f'O preço com 5% de desconto é R${desconto}')