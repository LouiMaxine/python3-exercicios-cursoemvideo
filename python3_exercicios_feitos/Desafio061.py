#Refaça o Desafio051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <=10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont+=1
print('FIM')