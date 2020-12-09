#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
# uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
s = 'S'
while s != 'N':
    r = int(input('Digite um valor: '))
    if r not in lista:
        lista.append(r)
    else:
        print('Valor já existe')
    s = str(input('Quer continuar? [S/N]')).upper()
lista.sort()
print(lista)

#Programa de Guanabara

#numeros = []
#while True:
 #  n = int(input('Digite um valor:'))
  # if n not in numeros:
   #    numeros.append(n)
    #   print('Valor adicionado com sucesso!')
   #else:
    #   print('Valor duplicado, não será adicionado')
   #r = str(input('Quer continuar? [S/N] ')).upper()
   #if r in 'Nn':
    #   break
#numeros.sort()
#print(f'Você digitou: {numeros}')

