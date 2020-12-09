'''FUPQ leia três números e mostre qual é o maior e qual é o menor'''

'''n1 = int(input('número 1: '))
n2 = int(input('Número dois: '))
n3 = int(input('Número 3: '))
if n1>n2>n3:
    print(f'Maior: {n1}; Menor: {n3}')
if n2>n1>n3:
    print(f'Maior: {n2}; Menor: {n3}')
if n3>n1>n2:
    print(f'Maior: {n3}; Menor: {n2}')
if n3>n2>n1:
    print(f'Maior: {n3}; Menor: {n1}')
if n1>n3>n2:
    print(f'Maior: {n1}; Menor: {n2}')
if n2>n3>n1:
    print(f'Maior: {n2}; Menor: {n1}')'''

a = int(input('Número 1: '))
b = int(input('Número2 : '))
c = int(input('Número 3: '))
#Verificando quem é o menor
menor = a
if c>b<a:
    menor = b
if b>c<a:
    menor = c

#Verificando quem é o maior
maior = a
if c<b>a:
   maior = b
if b<c>a:
    maior = c
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')




