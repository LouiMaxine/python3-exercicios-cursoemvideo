#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção
# inteira.
#Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6

'''from math import floor
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n,floor(n)))'''

#GUANABARA'S VERSION
'''from math import trunc
n = float(input('Número: '))
print('O número {} tem a parte inteira {}'.format(n,trunc(n)))'''


          #OU
n = float(input('Digite número: '))
print('O número {} tem a parte inteira {}'.format(n,int(n)))
