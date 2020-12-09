'''FUPQ jogue par ou ímpar com o PC. O jogo só será interrompido quando o jogador perder, mostrando o
total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
cont=0
while True:
    c = randint(0,10)
    n = int(input('Digite um número entre 0 e 10: '))
    p = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
    soma = c + n
    resultado = ''
    if soma %2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if p == 'P' and resultado == 'PAR' or p == 'I' and resultado == 'ÍMPAR':
        cont+=1
        print(f'O número que eu pensei foi {c} e somado com {n} dá o número {soma} que é {resultado}! Você Venceu')
    else:
        print(f'Eu pensei em {c} e somado com {n} é {soma}, que é {resultado}. Você perdeu')
        print(f'Seu número de conquistas foi {cont}')
        break
