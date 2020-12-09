'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''

for i in range(2,51,2): #Por pular de dois em dois, ele fez metade do trabalho, ocupou metade do espaço no processador e
                        # deu O MESMO RESULTADO
    if i%2==0:
        print(i, end=' ')