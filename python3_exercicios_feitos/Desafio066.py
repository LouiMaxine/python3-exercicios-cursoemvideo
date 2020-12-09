'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles. (desconsiderando o flag).'''

s = cont = 0
while True:
    num = int(input('Digite um valor: '))
    if num != 999:
        s +=num
        cont += 1
    else:
        break
print(f'A soma dos {cont} digitados, é {s} ')