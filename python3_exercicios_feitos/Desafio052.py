#FUPQ leia um número e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
total = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[31m',end=' ')
        total+=1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c),end = ' ')
print(f'O número {num} foi divisível {total} vezes')
if total == 2:
    print('E por isso é É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')




