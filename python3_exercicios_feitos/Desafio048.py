#Faça um programa que calcula a soma entre todos os numeros ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cont=0
cont2 = 0
for i in range(1,501, 2):
    if i%3==0:
        cont+=i
        cont2 += 1 #Para saber quanto números foram somados
print(f'O somatório dos {cont2} múltiplos de 3, ímpares, é {cont}')