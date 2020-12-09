#FUPQ tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-las dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

#def sorteio(numeros):
 #   for i in range(0,5):
  #      numeros.append(0,100)
   #     print(numeros)


#def somaPar(numeros):
 #   s = 0
  #  while len(numeros)!=0:
   #     if numeros[0]%2==0:
    #        s += numeros[0]
     #       numeros.remove()
    #print(f'A soma entre os número pares é {s}')


#numeros =[4,2,3]
#somaPar(numeros)

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(1)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor%2 ==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)








