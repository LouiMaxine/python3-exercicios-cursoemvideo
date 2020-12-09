'''FUPQ leia uma frase pelo teclado e mostre:
'Quantas vezes aparece a letra 'A'
Em q posição ela aparece a primeira vez
Em que posição ela aparece a última vez '''

frase=str(input('Frase: ')).strip().upper()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)