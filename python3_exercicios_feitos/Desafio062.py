#Melhore o Desafio061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total +=mais
    while cont <=total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer colocar a mais? '))
print('Progressão finalizada com {} termos mostrando'.format(total))