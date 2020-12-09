#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
temp = int(input('Temperatura em Celsius: '))
conversao = 9*temp/5+32
print(f'{temp}Cº equivale a {conversao}Fº')