'''FUPQ leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
Ex: Digite o número: 1834
unidade: 4
dezena:3
centena: 8
milhar: 1'''

'''nome = input('Digite um número: ')
print(f'Unidade: {nome[3]}')
print(f'Dezena: {nome[2]}')
print(f'Centena: {nome[1]}')
print(f'Milhar: {nome[0]}')'''

#GUANABARA'S MATH VERSION
num = int(input('Digite número: '))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print(f'Unidade = {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')