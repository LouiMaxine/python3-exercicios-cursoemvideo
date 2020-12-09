#Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

'''from random import randint
tentativa = 0
computador = randint(0,10)
jogador = int(input('Acerte o número em que estou pensando entre 0 e 10: '))
while jogador != computador:
    jogador = int(input('Você errou tente novamente: '))
    tentativa +=1
    if jogador == computador:
        print('Congratulations! Você acertou!')
print('Seu número de tentativas foi {}'.format(tentativa))'''

#GUANABARA'S VERSION
from random import randint
computador = randint(0,10)
tentativa = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativa +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {tentativa} tentativas. Parabéns!')
