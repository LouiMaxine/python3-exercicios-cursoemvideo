'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato'''

val = reais = menor = cont = 0
nome = ''
while True:
    produto = input('Produto: ')
    preco = float(input('Preço: '))
    cont+=1
    reais += preco
    if preco > 1000:
        val += 1
    if cont == 1 or preco <menor: #Serve para substituir o else de baixo que repete as mesmas coisas. economiza linhas
        menor = preco
        nome = produto
    '''else:
        if preco < menor:
            menor = preco
            nome = produto'''
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print(f'O total gasto na compra foi de R${reais}, {val} produtos custam mais de R$1000, e o produto mais barato custa R$ {menor} e o nome é {nome}')
        break
