'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome
'Santo' '''

'''cid = str(input('Nome da cidade: '))
if cid.upper().find('SANTO') == 0:
    print('True')
else:
    print('False')'''

cid = str(input('Cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')