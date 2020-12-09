'''FUPQ mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.'''

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    multi = 1
    while multi < 11:
        resultado = num*multi
        print(f'{num} x {multi} = {resultado}')
        multi+=1
    print('=-'*20)
print(' TABUADA ENCERRADA')