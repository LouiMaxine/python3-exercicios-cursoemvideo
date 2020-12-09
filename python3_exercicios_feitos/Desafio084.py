#FUPQ leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a - Quantas pessoas foram cadastradas b - Uma listagem com as pessoas mais pesadas.
# c - Uma listagem com as pessoas mais leves

#galera = []
#listaAux = []
#s = 'S'
#pesoMaior = pesoMenor = 0
#while s == 'S':
 #   listaAux.append(str(input('Nome: ')))
  #  listaAux.append(int(input('Peso: ')))
   # galera.append(listaAux[:])
    #listaAux.clear()
    #s = str(input('Quer continuar? [S/N]')).upper()
#print(f'Foram cadastradas {len(galera)} pessoa(s)')
#for p in galera:
 #   pesoMaior = pesoMenor = p[1]
  #  if p[1]>pesoMaior:
   #     pesoMaior = p[1]
    #    print(f'As pessoas mais pesadas são {pesoMaior}')

listaTemp = []
lisPrinc = []
mai = men = 0
while True:
    listaTemp.append(str(input('Nome: ')))
    listaTemp.append(float(input('Peso: ')))
    if len(lisPrinc) ==0:
        mai = men = listaTemp[1]
    else:
        if listaTemp[1]>mai:
            mai = listaTemp[1]
        if listaTemp[1]< men:
            men = listaTemp[1]
    lisPrinc.append(listaTemp[:])
    listaTemp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f"Vc cadastrou {len(lisPrinc)} pessoas")
print(f'O maior peso foi de {mai}kg. Peso de ',end='')
for p in lisPrinc:
    if p[1] == mai:
        print(f'{p[0]}')
print()
print(f'O menor peso foi o de {men}kg. Peso de ',end='')
for p in lisPrinc:
    if p[1] == men:
        print(f'{p[0]}', end="")
print()





