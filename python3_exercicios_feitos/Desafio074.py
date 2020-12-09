'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint
cont = 0
for c in range(0,5):
    tupla = randint(0,10)
    print(tupla, end=' ')
    cont+=1
    if cont == 1:
        menor = maior = c
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'O maior número sorteado é {maior}, e o menor {menor}')

