# Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso


from random import randint
val1 = int(input('Valor 1: '))
val2 = int(input('Valor 2: '))
print('='*10)
print('''O que você quer fazer? 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa''')
açao = 0
print('='*10)

while açao != 5:
    açao = int(input('Código: '))
    if açao == 1:
        print(f'A soma de {val1} e {val2} é: {val1+val2:.1f}')
    if açao == 2:
        print(f'Multiplicando {val1} com {val2}, obtemos: {val1*val2:.1f}')
    if açao == 3:
        if val1>val2:
            print(f'Entre {val1} e {val2} o maior número é: {val1}')
        else:
            print(f'Entre os valores {val1} e {val2} o maior é: {val2}')
    if açao == 4:
        novo1 = randint(0,10)
        novo2 = randint(0,10)
        print(f'Os novos valores são {novo1} e {novo2}')
print('Programa finalizado')

