#FUPQ leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.
l = float(input('Largura: '))
a = float(input('Altura: '))
area = a*l
print(f'A área da parede é {area}m^2 e a quantidade de tinta é de {area/2.0}l')