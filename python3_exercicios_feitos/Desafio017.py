#FUPQ leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento
# da hipotenusa
from math import hypot
catO = float(input('Cateto Oposto: '))
catA = float(input('Cateto Adjascente: '))
#hipotenusa = (catO **2 + catA ** 2)**(1/2)      cálculo da hipotenusa sem módulo
print('A hipotenusa desse triângulo é {:.2f}'.format(hypot(catA,catO)))