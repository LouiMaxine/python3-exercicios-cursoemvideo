#FUPQ tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(largura,comprimento):
    s = largura*comprimento
    print(f'A área do terreno de {largura}x{comprimento} é de {s}m^2')

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura,comprimento)