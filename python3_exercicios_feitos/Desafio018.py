#FUPQ leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
ang=int(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno do ângulo {}º, é: {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang,seno,cos,tang))
