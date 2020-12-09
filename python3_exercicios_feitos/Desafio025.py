'''Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva no nome'''

'''nome = str(input('Nome: '))
if nome.upper().find('SILVA') == -1:
    print('False')
else:
    print('True')'''

#GUANABARA'S VERSION

nome = str(input('Nome Completo: ')).strip()
print('SILVA'in nome.upper())
