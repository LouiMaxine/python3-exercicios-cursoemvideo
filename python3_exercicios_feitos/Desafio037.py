'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''


num = int(input('Qual é o número que você quer converter? '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
cod = int(input('Qual será a base de conversão? [1/2/3] '))
if cod == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}') #O 2: é a aula de fatiamento, para mostrar da posição 2 em diante
elif cod == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}')
elif cod == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Código inválido, tente novamente.')





