'''Crie um programa que simula o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual é o valor a ser sacado, ( número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20 R$ 10 e R$1'''

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual é o valor a ser sacado? R$'))
total = valor
ced = 50
totalcedula = 0
while True:
    if total>= ced:
        total -= ced
        totalcedula+=1
    else:
        if totalcedula >0:
            print(f'Total de {totalcedula} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced = 1
        totalcedula = 0
        if total == 0:
            break

