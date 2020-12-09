#FUPQ leia o peso de cinco pessoas. No fianal, mostre qual foi o maior e o menor peso lidos


maior = menor = 0
for p in range(0,5):
    peso = float(input('Digite o seu peso: '))
    if p==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor foi {menor}')



