'''FUPQ leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

m = str(input('Digite nome: ')).strip()
nome = m.split()
print(f'Primeiro = {nome[0]}')
print(f'Último = {nome[len(nome)-1]}')

