#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.
#usar contador, maior de idade com 21

from datetime import date
menor = 0
maior = 0
for p in range(0,7):
    nasc = int(input('Ano de Nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 21:
        maior+=1
    else:
        menor +=1
print(f'Das 7 pessoas, {maior} são maiores de idade e {menor} não são')




