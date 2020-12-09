'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos'''

anos18 = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        anos18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    c = ' '
    while c not in 'SN':
        c = str('Quer continuar? [S/N] ').strip().upper()[0]
    if c == 'N':
        break
print(f'Tem {anos18} maiores de 18 anos, {homens} homens, e {mulheres} com menos de 20 anos')
