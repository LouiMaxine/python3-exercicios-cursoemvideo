#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag - o 999)

'''cont = soma = num = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num !=999:
        soma += num
        cont+=1
print(f'Foram digitados {cont} números, que somados dão {soma}')'''

#GUANABARA'S VERSION
cont = soma = num = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont+=1
    num = int(input('Digite um número: '))
print(f'Foram digitados {cont} números, que somados dão {soma}')
