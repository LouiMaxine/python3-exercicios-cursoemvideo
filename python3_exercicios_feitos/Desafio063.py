#Escreva um programa que leia um número número n inteiro qualquer  e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci.
#Ex: 0-1-1-2-3-5-8

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
num = int(input('Quantos termos você quer mostrar?  '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1,t2), end='')
cont = 3 #já mostrei o primeiro e o segundo termo, por isso meu contador já começa no 3
while cont <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont+=1
print('-> FIM')
print('-'*30)
