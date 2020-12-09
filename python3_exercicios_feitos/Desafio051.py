#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética(Pa). No final, mostre 10 primeiros termos dessa prograssão.


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro+(10-1)*razão #Este é o cálculo de progressão aritmética (colocamos 10, por que queremos o décimo termo
for c in range(primeiro,decimo + razão,razão):
    print('{}'.format(c),end = '.')
print('ACABOU')
