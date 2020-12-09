#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
# deverá escrever na tela se o usuárip venceu ou perdeu

'''from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "pensar"
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns! You win!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,jogador))'''

from random import randint
pc = randint(0,5)
chute = int(input('Em qual número de 0 a 5 estou pensando? '))
if chute == pc:
    print('Parabéns! Você é incrível')
else:
    print('Que pena, você errou')
print(pc)


