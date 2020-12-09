'''Crie um programa que faça o computador jogar Jokempô com você'''

from random import choice
computador = ['PEDRA','PAPEL','TESOURA']
choice(computador)
jogador = str(input('Escolha entre Pedra, Papel e Tesoura: ')).upper()
if jogador == computador:
    print('O jogo empatou')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('Haha! Papel enrola Pedra, Eu venci!')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('Aff... Pedra quebra tesoura, Você venceu!')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('Aff... Papel enrola Pedra, Você venceu!')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('Haha! Tesoura corta papel, Eu venci!')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('Haha! Pedra quebra tesoura, Eu venci!')
else:
    print('Aff... Tesoura corta papel, Você venceu!')






