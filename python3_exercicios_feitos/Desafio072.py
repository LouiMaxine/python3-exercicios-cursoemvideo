'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até
vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito','dezenove','vinte' )
while True:
    tec = int(input('Digite um número entre 0 e 20: '))
    for n in enumerate(num):
        if tec in num[0:20]:
            break

print(f'Você digitou o número {num[tec]}')


