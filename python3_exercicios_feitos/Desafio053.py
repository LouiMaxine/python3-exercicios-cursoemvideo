#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os
# espaços
#Frases que podem ser lidas de trás pra fente e vai ser igual

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso= ''
inverso = junto[::-1] #macete do fatiamento no python
'''for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')





