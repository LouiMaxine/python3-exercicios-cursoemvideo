'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome'''

nome = str(input('Seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
#print(len(nome.split()[0])) '''esse tá certo, mas pode ser tbm:'''
#print(nome.find(' '))

#Guanabara's outra forma:
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

