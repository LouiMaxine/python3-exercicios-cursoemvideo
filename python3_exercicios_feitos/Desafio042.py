'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iuais
- Escaleno: todos os lados diferentes'''

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 <(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    print('As retas podem formar um triângulo')
    if  r1 ==r2 ==r3:
        print('EQUILÁTERO')
    elif r1 != r2 !=r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas NÃO formam um triângulo')






